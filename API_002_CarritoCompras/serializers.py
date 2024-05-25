from rest_framework import serializers
from .models import Carrito, CarritoItem
from inventario.models import Producto
from .services import get_active_cart

class CarritoItemSerializer(serializers.ModelSerializer):
    producto_id = serializers.PrimaryKeyRelatedField(
        queryset=Producto.objects.all(),
        source='producto',
        write_only=True
    )
    producto = serializers.StringRelatedField(read_only=True)
    precio_unitario = serializers.DecimalField(source='producto.precio', max_digits=10, decimal_places=2, read_only=True)
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = CarritoItem
        fields = ['producto_id', 'producto', 'cantidad', 'precio_unitario', 'subtotal']

    def get_subtotal(self, obj):
        return f'{obj.producto.precio * obj.cantidad:.2f}'

class CarritoSerializer(serializers.ModelSerializer):
    items = CarritoItemSerializer(many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Carrito
        fields = ['id', 'fecha_creacion', 'items', 'total']

    def get_total(self, obj):
        total = sum(item.producto.precio * item.cantidad for item in obj.items.all())
        return f'{total:.2f}'

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        carrito = get_active_cart()
        for item_data in items_data:
            producto = item_data.get('producto')
            cantidad = item_data.get('cantidad')
            item, created = CarritoItem.objects.get_or_create(
                carrito=carrito,
                producto=producto,
                defaults={'cantidad': cantidad}
            )
            if not created:
                item.cantidad += cantidad
                item.save()
        return carrito