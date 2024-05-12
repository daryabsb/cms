from django.contrib import admin

from src.hud.models import ProductGroup

@admin.register(ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    pass