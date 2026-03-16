from django.http import JsonResponse
from .models import ProductModule

def product_list(request):
    products = ProductModule.objects.all()

    data = []
    for product in products:
        data.append({
            "productName": product.productName,
            "price": product.price,
        })

    return JsonResponse(data, safe=False)