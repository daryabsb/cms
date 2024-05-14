from django.shortcuts import get_object_or_404, render
from src.hud.models import ProductGroup, Product, Barcode, PosOrderItem


def modal_product(request, id):
    product = get_object_or_404(Product, id=id)

    if product:
        context = {"product": product}
        return render(request, 'hud/pos/product-modal.html', context)



def add_quantity(request, item_number):
    item = get_object_or_404(PosOrderItem, number=item_number)
    item.quantity += 1  # Set quantity to the new value received from the client
    item.save()
    return render(request, 'hud/pos/partials/order-item-detail.html', {"item":item})

def subtract_quantity(request, item_number):
    item = get_object_or_404(PosOrderItem, number=item_number)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
        return render(request, 'hud/pos/partials/order-item-detail.html', {"item":item})
    elif item.quantity == 1:
        return render(request, 'hud/pos/renders/confirm-remove.html', {"item":item})