from django.contrib import admin

from src.hud.models import Customer, CustomerDiscount


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomerDiscount)
class CustomerDiscountAdmin(admin.ModelAdmin):
    pass
