from django import template
from loguru import logger
from django.urls import resolve
from django.urls.exceptions import Resolver404
from src.hud.models import PosOrder, PosOrderItem

register = template.Library()

# This the custom filter, name is getitems


def gettotals():
    func_name = ''
    # active_order = PosOrder.objects.filter(is_active=True).first()
    try:

        # logger.debug("Active Order is:> {} ",
        #              active_order.user.email, feature="f-strings")
        # logger.debug("Module Name:> {} ",
        #              myfunc.__module__, feature="f-strings")
        # logger.debug("URL_Path:> {} ", args, feature="f-strings")
        # func_name = myfunc.__name__
        print()
        logger.success("*"*50)
    except Resolver404:
        logger.debug("something went wrong", feature="f-strings")
        pass

    # return json_data.get(func_name)
    # return active_order.items


register.filter('gettotals', gettotals)
