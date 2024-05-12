from django.contrib import admin

from src.hud.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass