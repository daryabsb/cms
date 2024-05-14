from django.db import models
from src.accounts.models import User
from django.db.models import F, Sum


class PosOrder(models.Model):

    # number = models.CharField(
    #     max_length=100, primary_key=True, db_index=True, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders")
    discount = models.SmallIntegerField(default=0)
    discount_type = models.SmallIntegerField(default=0)
    # subtotal = models.GeneratedField(expression=Sum("items__subtotal"),
    #                                 output_field=models.DecimalField(
    #                                 max_digits=6, decimal_places=2
    #                                 ), db_persist=True,)
    total = models.FloatField(default=0)
    status = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # objects = OrderManager()
    class Meta:
        ordering = ['-created']
    
    @property
    def subtotal(self):
        return self.items.aggregate(
            total=Sum(F('price') * F('quantity')))['total'] or 0
    # def __str__(self):
    #     return f"{self.number}:" + \
    #         f" [{self.total}]" + \
    #         f" ({'Completed' if self.status else 'Pending'})"
