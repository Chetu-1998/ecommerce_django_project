from rest_framework import serializers

from productModule.models import ProductModule
from .models import CartModule


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModule
        fields = ['id', 'name', 'description', 'price', 'image']


class CartModuleSerializer(serializers.ModelSerializer):
    product = CartProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=ProductModule.objects.all(),
        source='product',
        write_only=True
    )

    class Meta:
        model = CartModule
        fields = '__all__'
        read_only_fields = ['user']