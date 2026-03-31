from django.db import models
from django.utils import timezone


class ProductModule(models.Model):
    name = models.CharField(max_length=255, default="Temporary Name")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='products/images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
