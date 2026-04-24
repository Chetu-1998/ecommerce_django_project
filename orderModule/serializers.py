from rest_framework import serializers
from .models import OrderModule

class OrderModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModule
        fields = '__all__'