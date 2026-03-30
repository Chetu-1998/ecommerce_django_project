from rest_framework.response import Response
from .models import ProductModule
from rest_framework import status
from .serializers import ProductSerializer
from rest_framework.decorators import api_view, permission_classes
from user.serializers import UserSerializer
from django.contrib.auth import get_user_model
from .permissions import IsAdminUserRole, IsUserRole


@api_view(['POST'])
@permission_classes([IsAdminUserRole])
def addProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsUserRole])
def viewProducts(request):
    products = ProductModule.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['PATCH'])
@permission_classes([IsAdminUserRole])
def updateProduct(request, id):
    try:
        product = ProductModule.objects.get(id=id)
    except ProductModule.DoesNotExist:
        return Response(
            {"message": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProductSerializer(product, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUserRole])
def deleteProduct(request, id):
    try:
        product = ProductModule.objects.get(id=id)
        product.delete()
        return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except ProductModule.DoesNotExist:
        return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsUserRole])
def viewProduct(request, id):
    try:
        product = ProductModule.objects.get(id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except ProductModule.DoesNotExist:
        return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
