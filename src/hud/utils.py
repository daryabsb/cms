from django.db import transaction
from src.hud.models import PosOrder

def activate_order_and_deactivate_others(order_id=None):
    with transaction.atomic():
        if order_id:
            order = PosOrder.objects.select_for_update().get(pk=order_id)
        else:
            order = PosOrder.objects.select_for_update().first()
            if not order:
                # If all orders are already active, just return None
                return None

        order.is_active = True
        order.save(update_fields=['is_active'])

        # Deactivate all other orders of the same user
        PosOrder.objects.filter(user=order.user).exclude(pk=order.pk).update(is_active=False)

    return order