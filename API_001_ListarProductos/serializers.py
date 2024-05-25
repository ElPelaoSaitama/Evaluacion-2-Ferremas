from rest_framework import serializers
from inventario.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'descripcion', 'marca', 'stock', 'fecha_llegada']
