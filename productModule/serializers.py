from rest_framework import serializers
from .models import ProductModule

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModule
        fields = '__all__'