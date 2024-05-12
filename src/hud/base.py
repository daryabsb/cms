from django.db import models
import uuid as uuid_lib
from django.urls import reverse
from src.hud.modules import upload_image_file_path


class BaseModel(models.Model):
    number = models.UUIDField(default=uuid_lib.uuid4,
                                primary_key=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseAddress(models.Model):
    tax_number = models.CharField(max_length=200, default="N/A")
    address = models.CharField(max_length=200, null=True, blank=True)
    postal_code = models.CharField(max_length=20, default='00000')
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, default="Iraq")
    street = models.CharField(max_length=350, null=True, blank=True)

    class Meta:
        abstract = True


class BaseNameModel(models.Model):
    name = models.CharField(max_length=200)
    handle = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def has_stores(self):
        return self.stores.exists()

    def get_absolute_url(self):
        return reverse(f"{self._meta.verbose_name_plural}:detail", kwargs={"handle": self.handle})

    def get_update_url(self):
        return reverse(f"{self._meta.verbose_name_plural}:update", kwargs={"handle": self.handle})

    @classmethod
    def get_create_url(cls):
        return reverse(f"{cls._meta.verbose_name_plural}:create", kwargs={})

    @property
    def display_name(self):
        return self.name


class ProductBase(models.Model):
    number = models.UUIDField(default=uuid_lib.uuid4,
                                primary_key=True, unique=True)
    user = models.ForeignKey("User",
                                default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    handle = models.SlugField(unique=True)
    # stripe_product_id = models.CharField(max_length=220, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    og_price = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    stripe_price = models.IntegerField(default=0)
    # stripe_price_id = models.CharField(max_length=220, null=True, blank=True)
    price_change_time = models.DateTimeField(
        auto_now_add=False, auto_now=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                                upload_to=upload_image_file_path)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def display_name(self):
        return self.name