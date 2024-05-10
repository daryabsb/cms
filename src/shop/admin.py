from django.contrib import admin
from src.shop.models import Product, ProductGroup, Order, OrderItem
# Register your models here.

admin.site.register(ProductGroup)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
