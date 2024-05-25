from .models import Carrito, CarritoItem
from inventario.models import Producto

def get_active_cart():
    carrito, created = Carrito.objects.get_or_create(activo=True)
    return carrito

def add_products_to_cart(items_data):
    carrito = get_active_cart()
    for item_data in items_data:
        producto = item_data['producto']
        cantidad = item_data['cantidad']
        item, created = CarritoItem.objects.get_or_create(
            carrito=carrito,
            producto=producto,
            defaults={'cantidad': cantidad}
        )
        if not created:
            item.cantidad += cantidad
            item.save()
    return carrito
