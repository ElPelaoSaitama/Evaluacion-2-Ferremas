from django.urls import path
from .api import ProductListView

urlpatterns = [
    path('productos/', ProductListView.as_view(), name='product-list'),
]
