from rest_framework import viewsets
from .serializer import VehiculoSerializer
from .models import Vehiculo


class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
