from django.urls import path
from .api import CarritoComprasView

urlpatterns = [
    path('carrito/', CarritoComprasView.as_view(), name='carrito-compras'),
]
