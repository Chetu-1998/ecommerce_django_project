from django.db import models
from productModule.models import ProductModule
from django.conf import settings


class CartModule(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        ProductModule,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user} - {self.product} ({self.quantity})"
