from django.contrib import admin

from src.hud.models import Tax, ProductTax


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductTax)
class ProductTaxAdmin(admin.ModelAdmin):
    pass
