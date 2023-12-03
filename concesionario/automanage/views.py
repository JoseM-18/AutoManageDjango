from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from .serializer import CotizacionSerializerDetailed, VehiculoSerializer, SucursalSerializer, PiezaSerializer,  UsuarioSerializer, RolSerializer, CotizacionSerializer, OrdenPiezaSerializer, PiezasVehiculoSerializer, InventarioPiezaSerializer, InventarioVehiculoSerializer, OrdenSerializer, VentaSerializer, ChangePasswordSerializer, VentaSerializerDetailed
from .models import Vehiculo, Sucursal, Pieza,  Usuario, Rol, Cotizacion, OrdenPieza, PiezasVehiculo, InventarioPieza, InventarioVehiculo, Orden, Venta
from .filters import *
from .permission import UserPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.decorators import action
from django.db.utils import IntegrityError
from rest_framework.permissions import IsAuthenticated, AllowAny


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
    filter_backends = [DjangoFilterBackend]
    filterset_class = SucursalFilter
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def listar_by_rol(self, request):
        user = request.user
        if user.is_admin or user.rol.nombre in ['Gerente']:
            queryset = self.get_queryset()
        else:
            queryset = Sucursal.objects.filter(id=user.sucursal.id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PiezaViewSet(viewsets.ModelViewSet):
    queryset = Pieza.objects.all()
    serializer_class = PiezaSerializer

    def destroy(self, request, *args, **kwargs):
        """
        Override the destroy method to customize object deletion.
        """
        instance = self.get_object()

        # Your custom logic goes here before deleting the object
        try:
            # Your custom logic goes here before deleting the object
            self.perform_destroy(instance)
        except IntegrityError as e:
            # Handle IntegrityError and return a 409 Conflict response
            return Response({"detail": "No es posible eliminar la Pieza por que se encuentra en uso."}, status=status.HTTP_409_CONFLICT)

        return Response(status=status.HTTP_204_NO_CONTENT)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UsuarioFilter

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

    @action(detail=False, methods=['GET'])
    def buscar_por_identificacion(self, request):
        identificacion = request.GET["identificacion"]
        try:
            usuario = Usuario.objects.get(identificacion=identificacion)
            serializer = self.get_serializer(usuario)
            return Response(serializer.data)
        except Usuario.DoesNotExist:
            return Response({"detail": "Usuario no encontrado"}, status=404)


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class CotizacionViewSet(viewsets.ModelViewSet):
    queryset = Cotizacion.objects.all()
    serializer_class = CotizacionSerializer

    def get_serializer_class(self):
        if self.action == 'detalle':
            return CotizacionSerializerDetailed
        return CotizacionSerializer

    @action(detail=False, methods=['GET'])
    def detalle(self, request):
        sucursal_id = self.request.query_params.get('sucursal_id')
        if sucursal_id:
            queryset = Cotizacion.objects.filter(
                inventario_vehiculos__sucursal__id=sucursal_id)
        else:
            queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class OrdenPiezaViewSet(viewsets.ModelViewSet):
    queryset = OrdenPieza.objects.all()
    serializer_class = OrdenPiezaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrdenPiezaFilter


class PiezasVehiculoViewSet(viewsets.ModelViewSet):
    queryset = PiezasVehiculo.objects.all()
    serializer_class = PiezasVehiculoSerializer


class InventarioPiezaViewSet(viewsets.ModelViewSet):
    queryset = InventarioPieza.objects.all()
    serializer_class = InventarioPiezaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = InventarioPiezaFilter


class InventarioVehiculoViewSet(viewsets.ModelViewSet):
    queryset = InventarioVehiculo.objects.all()
    serializer_class = InventarioVehiculoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = InventarioVehiculoFilter


class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

    def get_serializer_class(self):
        if self.action == 'detalle':
            return VentaSerializerDetailed
        return VentaSerializer

    @action(detail=False, methods=['GET'])
    def detalle(self, request):
        sucursal_id = self.request.query_params.get('sucursal_id')
        if sucursal_id:
            queryset = Venta.objects.filter(
                inventario_vehiculo__sucursal__id=sucursal_id)
        else:
            queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
