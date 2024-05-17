from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from src.hud.models import ProductGroup, Product, Barcode, PosOrderItem, PosOrder
from src.hud.calculations import add_or_update_product_to_order


def add_quantity(request, item_number):
    active_order = PosOrder.objects.filter(is_active=True).first()
    item = get_object_or_404(PosOrderItem, number=item_number)
    item.quantity += 1  # Set quantity to the new value received from the client
    item.save()

    context = {
        "item": item,
        "active_order": active_order,
    }
    return render(request, 'hud/pos/renders/update-order-item.html', context)


def subtract_quantity(request, item_number):
    active_order = PosOrder.objects.filter(is_active=True).first()
    item = get_object_or_404(PosOrderItem, number=item_number)
    context = {
        "item": item,
        "active_order": active_order,
    }
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
        return render(request, 'hud/pos/renders/update-order-item.html', context)
    elif item.quantity == 1:
        return render(request, 'hud/pos/renders/order-item-with-confirm.html', context)


def remove_item(request, item_number, is_button=False):
    '''
    Check if it is a direct delete
    '''
    if is_button:
        active_order = PosOrder.objects.filter(is_active=True).first()
        item = get_object_or_404(PosOrderItem, number=item_number)
        context = {
            "item": item,
            "active_order": active_order,
        }
        return render(request, 'hud/pos/renders/order-item-with-confirm.html', context)

    active_order = PosOrder.objects.filter(is_active=True).first()
    item = get_object_or_404(PosOrderItem, number=item_number)
    item.delete()

    context = {
        "active_order": active_order,
    }
    return render(request, 'hud/pos/renders/update-active-order.html', context)


def add_item_with_barcode(request):

    active_order = PosOrder.objects.filter(is_active=True).first()
    barcode_value = request.POST.get("barcode", None)
    barcode = get_object_or_404(Barcode, value=barcode_value)
    order = active_order
    total = 0
    item = PosOrderItem.objects.filter(
        order=active_order, product=barcode.product).first()

    if not item:
        order, item, total = add_or_update_product_to_order(
            request.user, barcode.product, active_order)
    else:
        item.quantity += 1
        item.save()

    context = {
        "item": item,
        "active_order": order,
        "total": total
    }
    return render(request, 'hud/pos/renders/update-active-order.html', context)


def add_order_item(request):
    active_order = PosOrder.objects.filter(is_active=True).first()
    if request.method == 'POST':
        product_id = request.POST.get('product_id', None)
        quantity = request.POST.get('quantity', 1)

        print("Quantity1 = ", quantity)

        order = active_order

        product = get_object_or_404(Product, id=product_id)

        item = PosOrderItem.objects.filter(
            order=active_order, product=product).first()

        if not item:
            order, subtotal, item = add_or_update_product_to_order(
                request.user, product, quantity, active_order)
        else:
            item.quantity += 1
            item.save()

        context = {
            "item": item,
            "items_subtotal": subtotal,
            "active_order": order,
        }

        return render(request, 'hud/pos/renders/update-active-order.html', context)

    return JsonResponse({"success": "Item added successfully!"})


def calculate(request):
    from django.http import JsonResponse
    print(dir(request))
    calculation = request.POST.get('calculation', '')
    # Process the calculation as needed, e.g., log it, store it, etc.
    print("calculation = ", calculation)
    return JsonResponse({'message': calculation})
