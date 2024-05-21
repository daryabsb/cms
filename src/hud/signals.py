from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from src.hud.models import Tax, ProductTax, PosOrder

@receiver(post_save, sender=Tax)
@receiver(post_delete, sender=Tax)
def update_orders_on_tax_change(sender, instance, **kwargs):
    update_active_orders()


@receiver(post_save, sender=ProductTax)
@receiver(post_delete, sender=ProductTax)
def update_orders_on_producttax_change(sender, instance, **kwargs):
    update_active_orders()


def update_active_orders():
    active_order = PosOrder.objects.filter(is_active=True).first()
    active_order.set_tax_fields()
    active_order.refresh_from_db()
    active_order.save()