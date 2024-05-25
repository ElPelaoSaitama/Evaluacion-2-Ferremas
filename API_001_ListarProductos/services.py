from inventario.models import Producto
from .serializers import ProductoSerializer

def get_all_active_products():
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return serializer.data
