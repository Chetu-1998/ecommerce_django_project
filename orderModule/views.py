from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from .serializers import OrderModuleSerializer
from .models import OrderItem, OrderModule
from productModule.models import ProductModule, Category
from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from cartModule.models import CartModule


@api_view(['GET'])
def dashboard_stats(request):
    totalProducts = ProductModule.objects.count()
    totalCategories = Category.objects.count()
    totalOrders = OrderModule.objects.count()
    totalRevenue = OrderModule.objects.aggregate(
        total_revenue=Sum('total_amount')
    )['total_revenue'] or 0

    data = {
        "totalProducts": totalProducts,
        "totalCategories": totalCategories,
        "totalOrders": totalOrders,
        "totalRevenue": totalRevenue
    }

    return JsonResponse(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def placeOrder(request):
    user = request.user

    cart_items = CartModule.objects.filter(user=user)

    if not cart_items.exists():
        return Response({"error": "Cart is empty"}, status=400)

    total_amount = 0

    order = OrderModule.objects.create(
        user=user,
        total_amount=0
    )

    for item in cart_items:
        product = item.product
        quantity = item.quantity

        if product.stock < quantity:
            return Response({
                "error": f"Only {product.stock} items available for {product.name}"
            }, status=400)

        price = product.price
        total_amount += price * quantity

        product.stock -= quantity
        product.save()

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=price
        )

    order.total_amount = total_amount
    order.save()

    cart_items.delete()

    return Response({
        "message": "Order placed successfully",
        "order_id": order.id,
        "total_amount": total_amount
    }, status=201)


@api_view(['GET'])
def viewOrders(request):
    orders = OrderModule.objects.all().order_by('-created_at') 
    serializer = OrderModuleSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteOrders(request):
    user = request.user

    orders = OrderModule.objects.filter(user=user)
    count = orders.count()

    orders.delete()

    return Response({
        "message": f"{count} orders deleted successfully"
    })