from django.http import JsonResponse
from .serializers import OrderModuleSerializer
from .models import OrderModule
from productModule.models import ProductModule, Category
from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
def placeOrder(request):
    serializer = OrderModuleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def viewOrders(request):
    orders = OrderModule.objects.all()
    serializer = OrderModuleSerializer(orders, many=True)
    return Response(serializer.data)
