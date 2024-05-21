from django.shortcuts import get_object_or_404, render
from src.hud.models import (
    ProductGroup, Product, Barcode, PosOrderItem, PosOrder,
    )
from src.hud.utils import activate_order_and_deactivate_others as aod, get_context
from src.hud.decorators import update_items_subtotal
# Create your views here.

def hud_index(request):
    return render(request, 'hud/index.html')

@update_items_subtotal
def hud_pos(request, id=None):

    active_order = aod(id)

    product_groups = ProductGroup.objects.all()
    pos_orders = PosOrder.objects.all()
    products = Product.objects.all()

    context = {
        "active_order":active_order,
        "groups": product_groups,
        "products": products,
        "orders": pos_orders,
    }

    return render(request, 'hud/pos/home.html', context)