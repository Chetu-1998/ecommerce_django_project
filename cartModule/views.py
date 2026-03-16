from django.http import JsonResponse
from .models import CartModule

def cart_list(request):
    carts = CartModule.objects.all()

    data = []
    for cart in carts:
        data.append({
            "cartName": cart.cartName,
            "cartNo": cart.cartNo,
        })

    return JsonResponse(data, safe=False)