from rest_framework import status
from .serializers import CartModuleSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import CartModule
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addToCart(request):
    user = request.user
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))

    try:
        cart_item = CartModule.objects.get(user=user, product_id=product_id)
        cart_item.quantity += quantity
        cart_item.save()

        serializer = CartModuleSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except CartModule.DoesNotExist:
        serializer = CartModuleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def viewCarts(request):
    carts = CartModule.objects.filter(user=request.user)
    serializer = CartModuleSerializer(carts, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeCart(request, id):
    try:
        cart = CartModule.objects.get(id=id)
        cart.delete()
        return Response({'message': 'Item removed from cart'}, status=status.HTTP_204_NO_CONTENT)
    except CartModule.DoesNotExist:
        return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def updateCart(request, id):
    try:
        cart = CartModule.objects.get(id=id)
        serializer = CartModuleSerializer(
            cart, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except CartModule.DoesNotExist:
        return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
