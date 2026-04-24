from django.utils import timezone
from django.db import models
from django.conf import settings

STATUS_CHOICES = [
    ('PENDING', 'Pending'),
    ('COMPLETED', 'Completed'),
    ('CANCELLED', 'Cancelled'),
]


class OrderModule(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=1)
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(default=timezone.now)


def __str__(self):
    return f"Order {self.status} - {self.total_amount}"
