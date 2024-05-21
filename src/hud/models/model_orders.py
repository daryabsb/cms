from django.db import models
from src.accounts.models import User
from django.db.models import F, Sum


class PosOrder(models.Model):

    # number = models.CharField(
    #     max_length=100, primary_key=True, db_index=True, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders")
    customer = models.ForeignKey(
        "Customer", on_delete=models.CASCADE, related_name="orders",
        null=True, blank=True, default=1)
    discount = models.SmallIntegerField(default=0)
    discount_type = models.SmallIntegerField(default=0)
    # item_subtotal = models.GeneratedField(expression=Sum(F("items__subtotal")),
    #                                       output_field=models.DecimalField(
    #     max_digits=15, decimal_places=3
    # ), db_persist=True,)
    item_subtotal = models.FloatField(default=0)
    total = models.FloatField(default=0)
    status = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # objects = OrderManager()
    class Meta:
        ordering = ['-created']

    def update_items_subtotal(self):
        # Calculate the subtotal based on order items
        self.item_subtotal = sum(item.item_total for item in self.items.all())
        self.save()

    @property
    def subtotal(self):
        return self.items.aggregate(
            total=Sum(F('price') * F('quantity')))['total'] or 0
    # def __str__(self):
    #     return f"{self.number}:" + \
    #         f" [{self.total}]" + \
    #         f" ({'Completed' if self.status else 'Pending'})"
