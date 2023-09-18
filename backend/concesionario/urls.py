from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inventario/', views.inventario, name='inventario'),
    path('pedido/', views.pedido, name='pedido'),
]