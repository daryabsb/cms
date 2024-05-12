from django.db import models
from src.accounts.models import User


class PosOrderItem(models.Model):
    number = models.CharField(
        max_length=100, primary_key=True, db_index=True, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="order_items"
    )
    order = models.ForeignKey(
        "PosOrder", on_delete=models.CASCADE, null=True, related_name="items"
    )
    product = models.ForeignKey(
        "Product", on_delete=models.DO_NOTHING, related_name="order_items"
    )
    round_number = models.DecimalField(
        decimal_places=3, max_digits=4, default=0)
    quantity = models.SmallIntegerField(default=1)
    price = models.DecimalField(decimal_places=3,  max_digits=9, default=0)
    is_locked = models.BooleanField(default=False)
    discount = models.FloatField(default=0)
    discount_type = models.FloatField(default=0)
    is_featured = models.BooleanField(default=False)
    # voide by = not comparable
    voided_by = models.SmallIntegerField(default=0)
    comment = models.TextField(null=True, blank=True)
    bundle = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name}: {self.quantity}{self.product.measurement_unit}"
