from django.urls import path, include
from rest_framework import routers
from automanage import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'vehiculos', views.VehiculoViewSet)
router.register(r'sucursales', views.SucursalViewSet)
router.register(r'piezas', views.PiezaViewSet)
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'roles', views.RolViewSet)
router.register(r'cotizaciones', views.CotizacionViewSet)
router.register(r'orden_piezas', views.OrdenPiezaViewSet)
router.register(r'piezas_vehiculo', views.PiezasVehiculoViewSet)
router.register(r'inventario_piezas', views.InventarioPiezaViewSet)
router.register(r'inventario_vehiculos', views.InventarioVehiculoViewSet)
router.register(r'ordenes', views.OrdenViewSet)
router.register(r'ventas', views.VentaViewSet)
# router.register(r'hello', views.HelloView.as_view())

urlpatterns = [
    path('', include(router.urls)),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('upload-image/', views.ImageUploadView.as_view(), name='upload-image')
]
