from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarritoSerializer
from .services import add_products_to_cart, get_active_cart

class CarritoComprasView(APIView):
    def post(self, request):
        serializer = CarritoSerializer(data=request.data)
        if serializer.is_valid():
            carrito = add_products_to_cart(serializer.validated_data['items'])
            return Response(CarritoSerializer(carrito).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        carrito = get_active_cart()
        serializer = CarritoSerializer(carrito)
        return Response(serializer.data, status=status.HTTP_200_OK)
