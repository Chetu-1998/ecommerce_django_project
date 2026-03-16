from django.http import JsonResponse
from .models import OrderModule

def order_list(request):
    orders = OrderModule.objects.all()

    data = []
    for order in orders:
        data.append({
            "orderName": order.orderName,
            "orderNo": order.orderNo,
        })

    return JsonResponse(data, safe=False)