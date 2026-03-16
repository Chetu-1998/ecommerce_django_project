from django.db import models

class OrderModule(models.Model):
    orderName = models.CharField(max_length=100)
    orderNo = models.IntegerField()

    def __str__(self):
        return self.orderName