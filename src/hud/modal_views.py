
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
    digits = [[7,8,9,'/'],[4,5,6,'*'],[1,2,3,'-'],[0,'.','=','+'],]
    context = {
        "div_class": div_class,
        "el_id": el_id,
        "url": url,
        "digits":digits,
    }
    return render(request, 'hud/pos/modals/calculator-modal.html', context)


def add_digit(request):
    if request.method == 'POST':
        current_value = request.POST.get('display', '')
        digit = request.POST.get('digit', '')
        new_value = current_value + digit
        return render(request, 'hud/pos/buttons/input_display.html', {'new_value': new_value})
    return render(request, 'keypad.html', {'error': 'Invalid request'})