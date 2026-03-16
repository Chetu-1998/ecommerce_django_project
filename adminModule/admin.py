from django.contrib import admin

from .models import AdminModule
# Register your models here.
class AdminModuleAdmin(admin.ModelAdmin):
    list_display = ('name','age')
admin.site.register(AdminModule, AdminModuleAdmin)
