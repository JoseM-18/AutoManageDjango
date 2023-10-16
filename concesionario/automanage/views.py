from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from .serializer import VehiculoSerializer, SucursalSerializer, PiezaSerializer,  UsuarioSerializer, RolSerializer, CotizacionSerializer, OrdenPiezaSerializer, PiezasVehiculoSerializer, InventarioPiezaSerializer, InventarioVehiculoSerializer, OrdenSerializer, VentaSerializer, ChangePasswordSerializer
from .models import Vehiculo, Sucursal, Pieza,  Usuario, Rol, Cotizacion, OrdenPieza, PiezasVehiculo, InventarioPieza, InventarioVehiculo, Orden, Venta
from .filters import *
from .permission import UserPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.decorators import action


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
    filter_backends = [DjangoFilterBackend]
    filterset_class = VehiculoFilter


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

    @action(detail=False, methods=['post'])
    def change_password(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']

            if not authenticate(email=user.email, password=old_password):
                return Response({'detail': 'La contraseña anterior es incorrecta'}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()

            return Response({'detail': 'Contraseña actualizada correctamente'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
