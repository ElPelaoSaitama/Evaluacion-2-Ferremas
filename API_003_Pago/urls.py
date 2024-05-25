from django.urls import path
from .api import PagoView

urlpatterns = [
    path('pago/', PagoView.as_view(), name='pago'),
]
