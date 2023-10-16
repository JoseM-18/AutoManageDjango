import django_filters
from .models import *


class VehiculoFilter(django_filters.FilterSet):

    class Meta:
        model = Vehiculo
        fields = {
            'marca': ['exact', 'contains'],
            'linea': ['exact'],
            'tipo': [],
            'precio': ['lt', 'gt', 'exact'],
        }
