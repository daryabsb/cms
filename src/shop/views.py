from django.shortcuts import render

# Create your views here.


def crm_shop_index(request):
    from src.shop.models import Order, OrderItem
    items = OrderItem.objects.all()
    if request.htmx:
        return render(request, 'crm/shop/orders/order-item.html')
    return render(request, 'crm/shop/home.html', {"items": items})
