from rest_framework import serializers
from .models import Pago, DetalleCompra
from API_002_CarritoCompras.models import CarritoItem , Carrito

class DetalleCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCompra
        fields = ['producto', 'cantidad', 'precio_unitario', 'subtotal']

class PagoSerializer(serializers.ModelSerializer):
    detalles = DetalleCompraSerializer(many=True, read_only=True)  # Ahora es de solo lectura

    class Meta:
        model = Pago
        fields = ['nombre_cliente', 'email_cliente', 'monto_total', 'detalles']

    def create(self, validated_data):
        # Obtener el carrito activo
        carrito = Carrito.objects.get(activo=True)
        
        # Generar los detalles de la compra a partir de los ítems del carrito
        detalles = []
        total = 0
        for item in carrito.items.all():
            detalle = DetalleCompra(
                producto=item.producto,
                cantidad=item.cantidad,
                precio_unitario=item.producto.precio,
                subtotal=item.cantidad * item.producto.precio
            )
            detalles.append(detalle)
            total += detalle.subtotal

        # Crear el pago con los detalles generados automáticamente
        pago = Pago.objects.create(
            nombre_cliente=validated_data['nombre_cliente'],
            email_cliente=validated_data['email_cliente'],
            monto_total=total
        )
        pago.detalles.set(detalles)

        # Limpiar el carrito
        carrito.items.all().delete()
        carrito.activo = False
        carrito.save()

        return pago
