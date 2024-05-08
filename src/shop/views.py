from django.shortcuts import render

# Create your views here.


def crm_shop_index(request):
    return render(request, 'crm/shop/home.html')