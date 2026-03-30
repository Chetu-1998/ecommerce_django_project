from django.contrib import admin

from .models import Category, ProductModule
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price')
admin.site.register(ProductModule, ProductAdmin)
admin.site.register(Category)