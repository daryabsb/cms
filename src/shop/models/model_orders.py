from django.db import models
from django.db.models import F


class Order(models.Model):
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.created}: {self.total}"


class OrderItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    product = models.ForeignKey(
        "Product", on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    quantity = models.SmallIntegerField(default=1)
    subtotal = models.GeneratedField(expression=F("price") * F("quantity"),
                                     output_field=models.DecimalField(
                                         max_digits=6, decimal_places=2
    ), db_persist=True,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name}: {self.quantity} X {self.price}"
