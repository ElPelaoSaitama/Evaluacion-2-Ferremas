from rest_framework import routers
from .api import MarcaViewSet, CategoriaViewSet, ProductoViewSet

router = routers.DefaultRouter()

router.register('api/marca',MarcaViewSet, 'marca' ),
router.register('api/categoria',CategoriaViewSet, 'categoria' ),
router.register('api/producto',ProductoViewSet, 'productos' )

urlpatterns = router.urls