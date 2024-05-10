from django.db import models


class ProductGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_group = models.ForeignKey("ProductGroup", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.name
