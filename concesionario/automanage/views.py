from rest_framework import viewsets
from .serializer import VehiculoSerializer, SucursalSerializer, PiezaSerializer,  UsuarioSerializer, RolSerializer, CotizacionSerializer, OrdenPiezaSerializer, PiezasVehiculoSerializer, InventarioPiezaSerializer, InventarioVehiculoSerializer, OrdenSerializer, VentaSerializer
from .models import Vehiculo, Sucursal, Pieza,  Usuario, Rol, Cotizacion, OrdenPieza, PiezasVehiculo, InventarioPieza, InventarioVehiculo, Orden, Venta
from .permission import UserPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password


class HelloView(APIView):
    permission_classes = [IsAuthenticated]
    # Ejemplo de como se van a manejar los accesos a cada endpoint:

    def get_permissions(self):
        return [UserPermission(
            roles_required=['Gerente', 'Jefe_Taller'])]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class VehiculoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
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

    def create(self, request, *args, **kwargs):
        password = request.data.get('password')
        hashed_password = make_password(password)
        request.data['password'] = hashed_password
        return super().create(request, *args, **kwargs)


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
