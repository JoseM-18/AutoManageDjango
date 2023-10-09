from rest_framework import viewsets
from .serializer import VehiculoSerializer, SucursalSerializer, PiezaSerializer,  UsuarioSerializer, RolSerializer, CotizacionSerializer, OrdenPiezaSerializer, PiezasVehiculoSerializer, InventarioPiezaSerializer, InventarioVehiculoSerializer, OrdenSerializer, VentaSerializer
from .models import Vehiculo, Sucursal, Pieza,  Usuario, Rol, Cotizacion, OrdenPieza, PiezasVehiculo, InventarioPieza, InventarioVehiculo, Orden, Venta
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer


class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer


class PiezaViewSet(viewsets.ModelViewSet):
    queryset = Pieza.objects.all()
    serializer_class = PiezaSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class CotizacionViewSet(viewsets.ModelViewSet):
    queryset = Cotizacion.objects.all()
    serializer_class = CotizacionSerializer


class OrdenPiezaViewSet(viewsets.ModelViewSet):
    queryset = OrdenPieza.objects.all()
    serializer_class = OrdenPiezaSerializer


class PiezasVehiculoViewSet(viewsets.ModelViewSet):
    queryset = PiezasVehiculo.objects.all()
    serializer_class = PiezasVehiculoSerializer


class InventarioPiezaViewSet(viewsets.ModelViewSet):
    queryset = InventarioPieza.objects.all()
    serializer_class = InventarioPiezaSerializer


class InventarioVehiculoViewSet(viewsets.ModelViewSet):
    queryset = InventarioVehiculo.objects.all()
    serializer_class = InventarioVehiculoSerializer


class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
