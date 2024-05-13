from django.contrib import admin

from src.hud.models import PosOrder

@admin.register(PosOrder)
class PosOrderAdmin(admin.ModelAdmin):
    pass