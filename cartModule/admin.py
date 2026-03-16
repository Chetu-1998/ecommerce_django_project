from django.contrib import admin

from .models import CartModule
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ('cartName','cartNo')
admin.site.register(CartModule, CartAdmin)
