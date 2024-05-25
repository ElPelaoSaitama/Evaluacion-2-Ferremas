from rest_framework import serializers
from inventario.models import Producto, Marca, Categoria


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializers(read_only=True)
    marca = MarcaSerializer(read_only=True)

    class Meta:
        model = Producto
        fields = '__all__'
        #fields = ['id', 'nombre', 'precio', 'descripcion', 'marca', 'stock', 'fecha_llegada']
