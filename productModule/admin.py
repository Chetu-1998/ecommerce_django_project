from django.contrib import admin

from .models import ProductModule
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('productName','price')
admin.site.register(ProductModule, ProductAdmin)
