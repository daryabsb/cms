from django.db import models
from src.accounts.models import User


class PosOrder(models.Model):

    # number = models.CharField(
    #     max_length=100, primary_key=True, db_index=True, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders")
    discount = models.SmallIntegerField(default=0)
    discount_type = models.SmallIntegerField(default=0)
    total = models.FloatField(default=0)
    status = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # objects = OrderManager()

    class Meta:
        ordering = ['-created']

    # def __str__(self):
    #     return f"{self.number}:" + \
    #         f" [{self.total}]" + \
    #         f" ({'Completed' if self.status else 'Pending'})"
