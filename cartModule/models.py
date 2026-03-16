from django.db import models

class CartModule(models.Model):
    cartName = models.CharField(max_length=100)
    cartNo = models.IntegerField(default=0)

    def __str__(self):
        return self.cartName