from django.shortcuts import render
from src.hud.models import ProductGroup, Product, Barcode

# Create your views here.

def hud_index(request):
    return render(request, 'hud/index.html')

def hud_pos(request):
    product_groups = ProductGroup.objects.all()
    products = Product.objects.all()
    context = {
        'groups': product_groups,
        'products': products,
    }
    return render(request, 'hud/pos/home.html', context)