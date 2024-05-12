from django.contrib import admin

from src.hud.models import Barcode

@admin.register(Barcode)
class BarcodeAdmin(admin.ModelAdmin):
    pass