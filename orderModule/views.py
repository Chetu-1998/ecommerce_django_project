from django.http import JsonResponse
from .models import OrderModule
from productModule.models import ProductModule, Category
from django.db.models import Sum
from rest_framework.decorators import api_view

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