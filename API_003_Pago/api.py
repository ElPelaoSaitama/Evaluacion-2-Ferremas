from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PagoSerializer
from .services import procesar_pago

class PagoView(APIView):
    def post(self, request):
        serializer = PagoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                pago = procesar_pago(serializer.validated_data)
                return Response(PagoSerializer(pago).data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
