from rest_framework import serializers
from .models import Producto , Marca , Categoria

class MarcaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializers(serializers.ModelSerializer):
    marca = MarcaSerializers(read_only=True)
    marca_id = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all(), source="marca")

    
    class Meta:
        model = Producto
        fields = '__all__'