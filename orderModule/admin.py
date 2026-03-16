from django.contrib import admin

from .models import OrderModule
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('orderName','orderNo')
admin.site.register(OrderModule, OrderAdmin)
