from django.contrib import admin

from src.hud.models import PosOrderItem

@admin.register(PosOrderItem)
class PosOrderItemAdmin(admin.ModelAdmin):
    pass