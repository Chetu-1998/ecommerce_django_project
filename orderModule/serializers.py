from rest_framework import serializers
from .models import OrderModule, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price']

    def get_product(self, obj):
        return {
            "id": obj.product.id,
            "name": obj.product.name,
            "image": obj.product.image.url if obj.product.image else None
        }


class OrderModuleSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    user = serializers.SerializerMethodField()

    class Meta:
        model = OrderModule
        fields = [
            'id',
            'user',
            'total_amount',
            'status',
            'created_at',
            'items'
        ]

        read_only_fields = [
            'total_amount',
            'created_at'
        ]

    def get_user(self, obj):
        return {
            "id": obj.user.id,
            "name": obj.user.username,
            "email": obj.user.email
        }
