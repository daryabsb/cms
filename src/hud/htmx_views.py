from django.shortcuts import get_object_or_404, render
from src.hud.models import ProductGroup, Product, Barcode, PosOrderItem, PosOrder


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