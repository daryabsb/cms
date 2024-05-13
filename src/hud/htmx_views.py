from django.http import JsonResponse
from decimal import Decimal
from django.shortcuts import get_object_or_404, render
from src.hud.models import ProductGroup, Product, Barcode, PosOrderItem


def modal_product(request, id):
    product = get_object_or_404(Product, id=id)

    if product:
        context = {"product": product}
        return render(request, 'hud/pos/product-modal.html', context)


# def add_quantity(request, item_number):
#     item = get_object_or_404(PosOrderItem, id=item_number)
#     item.quantity += 1
#     item.save()
#     return JsonResponse({"qty": item.quantity})


def add_quantity(request, item_number):
    if request.method == "POST":
        qty = request.POST.get("qty", 1)
        print("QTY = ", qty)
        item = get_object_or_404(PosOrderItem, number=item_number)
        item.quantity += Decimal(qty)
        print(item.quantity)
        # item.save()
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False, "error": "Invalid request method"})