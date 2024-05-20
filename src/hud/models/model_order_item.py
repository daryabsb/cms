from django.db import models
from src.accounts.models import User
from django.db.models import F, Sum, Case, When
from decimal import Decimal


class PosOrderItem(models.Model):
    DISCOUNT_TYPE_CHOICES = (
        (0, 'IQD'),
        (1, '%'),
    )
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
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(decimal_places=3,  max_digits=15, default=0)
    # subtotal = models.GeneratedField(
    #     expression=F("price") * F("quantity"),
    #     output_field=models.DecimalField(
    #         max_digits=15, decimal_places=3
    #     ), db_persist=True,)
    subtotal = models.DecimalField(decimal_places=3,  max_digits=15, default=0)
    is_locked = models.BooleanField(default=False)
    discount = models.FloatField(default=0)
    discount_type = models.PositiveSmallIntegerField(default=0, choices=DISCOUNT_TYPE_CHOICES)
    is_featured = models.BooleanField(default=False)
    # voide by = not comparable
    voided_by = models.SmallIntegerField(default=0)
    comment = models.TextField(null=True, blank=True)
    bundle = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name}: {self.quantity}{self.product.measurement_unit}"

    def save(self, *args, **kwargs):
        import random
        from datetime import date
        if not self.number:
            min = 100
            max = 3999
            digits = str(random.randint(min, max))
            digits = (len(str(max))-len(digits))*'0'+digits
            target = 'item'
            print(digits)
            if target:
                self.number = f'{target}-{self.user.id}-{date.today().strftime("%d%m%Y")}-01-{digits}'

        super(PosOrderItem, self).save(*args, **kwargs)
