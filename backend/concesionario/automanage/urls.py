from django.urls import path, include
from rest_framework import routers
from automanage import views

router = routers.DefaultRouter()
router.register(r'vehiculos', views.VehiculoViewSet)
router.register(r'sucursales', views.SucursalViewSet)
router.register(r'piezas', views.SucursalViewSet)
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'roles', views.RolViewSet)
router.register(r'cotizaciones', views.CotizacionViewSet)
router.register(r'orden_piezas', views.OrdenPiezaViewSet)
router.register(r'piezas_vehiculo', views.PiezasVehiculoViewSet)
router.register(r'inventario_piezas', views.InventarioPiezaViewSet)
router.register(r'inventario_vehiculos', views.InventarioVehiculoViewSet)
router.register(r'ordenes', views.OrdenPiezaViewSet)
router.register(r'ventas', views.VentaViewSet)

urlpatterns = [
    path('', include(router.urls))
]
