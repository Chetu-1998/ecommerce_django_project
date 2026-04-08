from django.db import models


class OrderModule(models.Model):
    # orderName = models.CharField(max_length=100)
    # orderNo = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


def __str__(self):
    return self.orderName
