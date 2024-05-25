from API_002_CarritoCompras.models import Carrito, CarritoItem
from inventario.models import Producto
from .models import Pago, DetalleCompra

def get_active_cart():
    carrito, created = Carrito.objects.get_or_create(activo=True)
    return carrito

def add_products_to_cart(items_data):
    carrito = get_active_cart()
    for item_data in items_data:
        producto = Producto.objects.get(id=item_data['producto_id'])
        item, created = CarritoItem.objects.get_or_create(
            carrito=carrito,
            producto=producto,
            defaults={'cantidad': item_data['cantidad']}
        )
        if not created:
            item.cantidad += item_data['cantidad']
            item.save()
    return carrito

def procesar_pago(data):
    carrito = get_active_cart()
    total_calculado = sum(item.producto.precio * item.cantidad for item in carrito.items.all())
    
    if total_calculado != data['monto_total']:
        raise ValueError("El monto total no coincide con el total del carrito.")
    
    pago = Pago.objects.create(
        nombre_cliente=data['nombre_cliente'],
        email_cliente=data['email_cliente'],
        monto_total=data['monto_total']
    )

    for item in carrito.items.all():
        DetalleCompra.objects.create(
            pago=pago,
            producto=item.producto,
            cantidad=item.cantidad,
            precio_unitario=item.producto.precio,
            subtotal=item.producto.precio * item.cantidad
        )
        item.producto.stock -= item.cantidad
        item.producto.save()
    
    carrito.items.all().delete()
    carrito.activo = False
    carrito.save()
    
    return pago
