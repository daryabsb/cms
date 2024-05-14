from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from src.hud.models import ProductGroup, Product, Barcode, PosOrderItem, PosOrder
from decimal import Decimal


def modal_product(request, id):
    product = get_object_or_404(Product, id=id)

    if product:
        context = {"product": product}
        return render(request, 'hud/pos/product-modal.html', context)


def add_quantity(request, item_number):
    item = get_object_or_404(PosOrderItem, number=item_number)
    item.quantity += 1  # Set quantity to the new value received from the client
    item.save()
    active_order = PosOrder.objects.filter(is_active=True).first()
    context = {
        "item": item,
        "active_order": active_order,
    }
    return render(request, 'hud/pos/renders/update-order-item.html', context)


def subtract_quantity(request, item_number):
    item = get_object_or_404(PosOrderItem, number=item_number)
    active_order = PosOrder.objects.filter(is_active=True).first()
    context = {
        "item": item,
        "active_order": active_order,
    }
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
        return render(request, 'hud/pos/renders/update-order-item.html', context)
    elif item.quantity == 1:
        return render(request, 'hud/pos/renders/confirm-remove.html', context)


def remove_item(request, item_number):
    active_order = PosOrder.objects.filter(is_active=True).first()
    item = get_object_or_404(PosOrderItem, number=item_number)
    item.delete()

    context = {
        "active_order": active_order,
    }
    return render(request, 'hud/pos/renders/update-active-order.html', context)


def add_order_item(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id', None)
        quantity_str = request.POST.get('quantity', '1')
        try:
            quantity = Decimal(quantity_str)
        except Decimal.InvalidOperation as e:
            print(e)
            # Handle the case where quantity is not a valid decimal
            return

        active_order = PosOrder.objects.filter(is_active=True).first()

        if product_id:
            product = get_object_or_404(Product, id=product_id)
            item = PosOrderItem.objects.filter(product=product).first()
            print("type(product.price) = ", type(product.price))
            if item:
                context = {
                    "item": item,
                    "active_order": active_order,
                }
                if quantity:
                    item.quantity += quantity

                    item.save()
                    return render(request, 'hud/pos/renders/update-active-order.html', context)
            else:
                item = PosOrderItem.objects.create(
                    user=request.user,
                    order=active_order,
                    product=product,
                    price=product.price + Decimal(0.00),
                    # quantity=int(quantity)
                )
                if quantity > 1:
                    item.quantity = quantity
                    item.save()
                context = {
                    "item": item,
                    "active_order": active_order,
                }
            return render(request, 'hud/pos/renders/update-active-order.html', context)
        else:
            return JsonResponse({"failed": "Failed to add!"})

    return JsonResponse({"success": "Item added successfully!"})
