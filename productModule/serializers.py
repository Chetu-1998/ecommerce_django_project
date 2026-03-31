from rest_framework import serializers
from .models import ProductModule, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModule
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
