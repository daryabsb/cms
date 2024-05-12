from django.shortcuts import get_object_or_404, render
from src.hud.models import ProductGroup, Product, Barcode


def modal_product(request, id):
    product = get_object_or_404(Product, id=id)

    if product:
        context = {"product": product}
        return render(request, 'hud/pos/product-modal.html', context)
