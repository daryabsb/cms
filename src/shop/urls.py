from django.urls import path
from src.shop.views import (
    crm_shop_index
)

app_name = 'shop'

urlpatterns = [
    path('', crm_shop_index, name='shop'),
]