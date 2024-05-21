from django.shortcuts import get_object_or_404, render
from src.hud.models import ProductGroup, Product, Barcode, PosOrderItem, PosOrder
from src.hud.calculations import (
    create_order_item,
)
from loguru import logger


def log(step, time):
    logger.success("*"*50)
    print()
    logger.debug("Step {}:> {} ", step, time, feature="f-strings")
    print()
    logger.success("*"*50)


def get_active_order(active_order=None):
    if not active_order:
        active_order = PosOrder.objects.filter(is_active=True).first()
    active_order.update_items_subtotal()
    active_order.refresh_from_db()
    # logger.success("Active order item_subtotal:> {} ", active_order.item_subtotal, feature="f-strings")
    # logger.success("Active order total:> {} ", active_order.total, feature="f-strings")
    return active_order


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
    item = get_object_or_404(PosOrderItem, number=item_number)
    quantity = request.POST.get("display", None)

    if quantity:
        item.quantity = quantity
        item.save()

    active_order = get_active_order()
    context = {"active_order": active_order, "item": item}
    return render(request, update_active_order_template, context)

def add_quantity(request, item_number):
    item = get_object_or_404(PosOrderItem, number=item_number)
    item.quantity += 1  # Set quantity to the new value received from the client
    item.save()
    # item = recalculate_item(order_item=item)
    active_order = get_active_order()
    context = {"active_order": active_order, "item": item}
    return render(request, update_active_order_template, context)

def subtract_quantity(request, item_number):
    item = get_object_or_404(PosOrderItem, number=item_number)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
        # item = recalculate_item(order_item=item)

        active_order = get_active_order()
        context = {"active_order": active_order, "item": item}
        return render(request, update_active_order_template, context)
    elif item.quantity == 1:

        active_order = get_active_order()
        context = {"active_order": active_order, "item": item}
        return render(request, order_item_confirm_remove_template, context)

def change_discount(request, item_number):
    item = get_object_or_404(PosOrderItem, number=item_number)
    # FIND A WAY TO ADD DISCOUNT
    item.quantity += 1  # Set quantity to the new value received from the client
    item.save()
    # item = recalculate_item(order_item=item)
    active_order = get_active_order()
    context = {"active_order": active_order, "item": item}
    return render(request, update_active_order_template, context)

def confirm_remove_item_button(request, item_number):
    item = get_object_or_404(PosOrderItem, number=item_number)

    active_order = get_active_order()
    context = {"active_order": active_order, "item": item}
    return render(request, order_item_confirm_remove_template, context)

def remove_item(request, item_number):
    item = get_object_or_404(PosOrderItem, number=item_number)
    item.delete()

    active_order = get_active_order()
    context = {"active_order": active_order}
    # context = get_context(active_order)

    return render(request, update_active_order_template, context)

def add_item_with_barcode(request):
    barcode_value = request.POST.get("barcode", None)
    barcode = get_object_or_404(Barcode, value=barcode_value)

    item = PosOrderItem.objects.filter(
        user=request.user, order=active_order, product=barcode.product).first()
    if item:
        item.quantity += 1  # Set quantity to the new value received from the client
        item.save()
    else:
        item = create_order_item(
            request.user,active_order,barcode.product
        )

    active_order = get_active_order()
    context = {"active_order": active_order, "item": item}
    return render(request, update_active_order_template, context)

def add_order_item(request):
    product_id = request.POST.get('product_id', None)
    quantity = int(request.POST.get('quantity', 1))
    active_order = get_active_order()

    product = get_object_or_404(Product, id=product_id)

    item = PosOrderItem.objects.filter(
        order=active_order, product=product).first()

    if not item:
        item = create_order_item(
            request.user,active_order,product, quantity)
    else:
        item.quantity += quantity
        item.save()

    active_order = get_active_order()
    context = {"active_order": active_order, "item": item}

    return render(request, update_active_order_template, context)


def calculate(request):
    from django.http import JsonResponse
    calculation = request.POST.get('display', '')
    # Process the calculation as needed, e.g., log it, store it, etc.
    print("calculation = ", calculation)
    return JsonResponse({'message': calculation})
