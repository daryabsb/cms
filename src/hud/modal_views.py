
from django.shortcuts import get_object_or_404, render
from src.hud.models import PosOrder, Product


def modal_product(request, id):
    active_order = PosOrder.objects.filter(is_active=True).first()
    product = get_object_or_404(Product, id=id)

    if product:
        context = {"product": product, "active_order": active_order}
        return render(request, 'hud/pos/modals/product-modal.html', context)


def modal_calculator(request):

    div_class = request.GET.get('div-class', '')
    el_id = request.GET.get('el-id', '')
    url = request.GET.get('url', '')
    template_name = request.GET.get('template-name', '')
    context = {
        "div_class": div_class,
        "el_id": el_id,
        "url": url
    }
    return render(request, 'hud/pos/modals/calculator-modal.html', context)
