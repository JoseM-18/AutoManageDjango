import django_filters
from .models import *


class VehiculoFilter(django_filters.FilterSet):

    class Meta:
        model = Vehiculo
        fields = {
            'marca': ['exact', 'contains', 'in'],
            'linea': ['exact'],
            'tipo': ['exact'],
            'precio': ['lt', 'gt', 'exact'],
        }


class SucursalFilter(django_filters.FilterSet):

    class Meta:
        model = Sucursal
        fields = {
            'nombre': ['exact', 'icontains', 'in'],
            'direccion': ['exact'],
            'fecha_creacion': ['lt', 'gt', 'exact'],
        }


class InventarioVehiculoFilter(django_filters.FilterSet):

    class Meta:
        model = InventarioVehiculo
        fields = {
            'vehiculo': ['exact', 'in'],
            'sucursal': ['exact', 'in'],
            'modelo': ['exact', 'lt', 'gt'],
            'condicion': ['exact'],
            'estado': ['exact'],
            'placa': ['exact', 'icontains', 'in'],
            'color': ['exact', 'icontains', 'in'],
            'kilometraje': ['lt', 'gt'],
        }
