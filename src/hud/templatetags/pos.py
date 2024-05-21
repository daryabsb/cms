from django import template
from loguru import logger
from django.urls import resolve
from django.urls.exceptions import Resolver404
from src.hud.models import PosOrder, PosOrderItem
from src.hud.utils import get_context

register = template.Library()

# This the custom filter, name is getitems


def gettotals(active_order):
    from src.hud.models import PosOrder
    return {
        "active_order": active_order,
        "order": PosOrder.objects.filter(is_active=True).first()
    }
register.filter('gettotals', gettotals)
