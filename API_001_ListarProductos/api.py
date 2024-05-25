from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import MethodNotAllowed
from .services import get_all_active_products

class ProductListView(APIView):
    def get(self, request):
        products = get_all_active_products()
        return Response(products, status=status.HTTP_200_OK)


    #Manejo de errores por metodo equivocado
    def handle_exception(self, exc):
        if isinstance(exc, MethodNotAllowed):
            return Response(
                {"Detalle": "Método no permitido. Por favor, usa el método GET."},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        return super().handle_exception(exc)
