from django import template
from loguru import logger
from django.urls import resolve
from django.urls.exceptions import Resolver404
from src.hud.models import PosOrder, PosOrderItem
from src.hud.utils import get_context

register = template.Library()

# This the custom filter, name is getitems


def gettotals(active_order):
    from src.hud.calculations import update_order_totals

    order, discount, tax_amount, tax_rate = update_order_totals(active_order)
    return {
        "active_order": order,
        "discount": discount,
        "tax_rate": tax_rate,
        "tax_amount": tax_amount,
        "dscnt": tax_amount
    }


register.filter('gettotals', gettotals)
