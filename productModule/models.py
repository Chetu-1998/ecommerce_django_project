from django.db import models

# Create your models here.

class ProductModule(models.Model):
    productName = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.productName