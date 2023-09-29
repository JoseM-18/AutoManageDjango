from django.urls import path, include
from rest_framework import routers
from automanage import views

router = routers.DefaultRouter()
router.register(r'vehiculos', views.VehiculoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
