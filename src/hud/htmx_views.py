from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from src.hud.models import ProductGroup, Product, Barcode, PosOrderItem, PosOrder
from src.hud.calculations import (
    add_or_update_product_to_order as add_or_create_item,
    calculate_subtotal_and_discounts as recalculate_item,
)
from src.hud.utils import get_context
from loguru import logger
from src.hud.decorators import update_items_subtotal


def log(step, time):
    logger.success("*"*50)
    print()
    logger.debug("Step {}:> {} ", step, time, feature="f-strings")
    print()
    logger.success("*"*50)


# update_active_order_template = 'hud/pos/renders/update-active-order.html'
update_active_order_template = 'hud/pos/order-detail.html'
update_order_item_template = 'hud/pos/renders/update-order-item.html'
order_item_confirm_remove_template = 'hud/pos/renders/order-item-with-confirm.html'


def time_function():
    import timeit
    starttime = timeit.default_timer()
    secondtime = timeit.default_timer()
    thirdtime = timeit.default_timer()
    fourthtime = timeit.default_timer()
    lasttime = timeit.default_timer()
    print("The secondtime is :", secondtime - starttime)
    print("The thirdtime is :", thirdtime - secondtime)
    print("The fourthtime is :", fourthtime - thirdtime)
    print("The lasttime is :", lasttime - fourthtime)


def p(arg):
    print(arg)


def change_quantity(request, item_number):
    active_order = PosOrder.objects.filter(is_active=True).first()
    item = get_object_or_404(PosOrderItem, number=item_number)
    quantity = request.POST.get("display", None)
    p(f"quantity: {quantity}")
    if quantity:
        item.quantity = quantity
        item.save()
    item = recalculate_item(order_item=item)

    context = get_context(active_order)
    context["item"] = item

    return render(request, update_active_order_template, context)


@update_items_subtotal
def add_quantity(request, item_number):
    active_order = PosOrder.objects.filter(is_active=True).first()
    item = get_object_or_404(PosOrderItem, number=item_number)
    item.quantity += 1  # Set quantity to the new value received from the client
    item.save()
    # item = recalculate_item(order_item=item)

    context = get_context(active_order)
    context["item"] = item

    return render(request, update_active_order_template, context)


def subtract_quantity(request, item_number):
    active_order = PosOrder.objects.filter(is_active=True).first()
    item = get_object_or_404(PosOrderItem, number=item_number)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
        item = recalculate_item(order_item=item)

        context = get_context(active_order)
        context["item"] = item
        return render(request, update_active_order_template, context)
    elif item.quantity == 1:
        item = recalculate_item(order_item=item)

        context = get_context(active_order)
        context["item"] = item

        return render(request, update_active_order_template, context)


def p(name, var=None):
    print(name, var)


def confirm_remove_item_button(request, item_number):
    active_order = PosOrder.objects.filter(is_active=True).first()
    item = get_object_or_404(PosOrderItem, number=item_number)
    context = get_context(active_order)
    context["item"] = item
    return render(request, order_item_confirm_remove_template, context)


def remove_item(request, item_number):

    active_order = PosOrder.objects.filter(is_active=True).first()
    item = get_object_or_404(PosOrderItem, number=item_number)

    item.delete()
    context = {"active_order": active_order}
    # context = get_context(active_order)

    return render(request, update_active_order_template, context)


def add_item_with_barcode(request):

    barcode_value = request.POST.get("barcode", None)
    active_order = PosOrder.objects.filter(is_active=True).first()
    barcode = get_object_or_404(Barcode, value=barcode_value)
    order = active_order

    item = PosOrderItem.objects.filter(
        user=request.user, order=active_order, product=barcode.product).first()
    if item:
        item.quantity += 1  # Set quantity to the new value received from the client
        item.save()
    # if not item:
    order, item = add_or_create_item(
        user=request.user, product=barcode.product, order=active_order)
    context = get_context(order)
    context["item"] = item
    return render(request, update_active_order_template, context)
    # else:
    #     item.quantity += 1
    #     item.save()

    #     context = get_context(order)
    #     context["item"] = item
    #     return render(request, update_order_item_template, context)


def add_order_item(request):
    import timeit
    active_order = PosOrder.objects.filter(is_active=True).first()

    product_id = request.POST.get('product_id', None)
    quantity = int(request.POST.get('quantity', 1))

    print("Quantity1 = ", quantity)

    order = active_order

    product = get_object_or_404(Product, id=product_id)

    item = PosOrderItem.objects.filter(
        order=active_order, product=product).first()

    if not item:
        order, item = add_or_create_item(
            user=request.user, product=product, quantity=quantity, order=active_order)
    else:
        item.quantity += quantity
        item.save()

    context = get_context(active_order)
    context["item"] = item

    return render(request, update_active_order_template, context)


def calculate(request):
    from django.http import JsonResponse
    calculation = request.POST.get('display', '')
    # Process the calculation as needed, e.g., log it, store it, etc.
    print("calculation = ", calculation)
    return JsonResponse({'message': calculation})
