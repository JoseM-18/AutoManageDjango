from rest_framework import serializers
from .models import Vehiculo, Sucursal, Pieza, Usuario, Rol, Cotizacion, OrdenPieza, PiezasVehiculo, InventarioPieza, InventarioVehiculo, Orden, Venta
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['user_email'] = user.email
        token['user_nombre'] = user.nombre
        token['user_apellido'] = user.apellido
        token['user_rol'] = user.rol.nombre
        token['user_sucursal_id'] = "" if user.sucursal is None else user.sucursal.id
        token['user_sucursal_nombre'] = "" if user.sucursal is None else user.sucursal.nombre
        # ...

        return token


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'


class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        # fields=('id_vehiculo','marca','linea')
        fields = '__all__'


class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'


class PiezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pieza
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    rol_id = serializers.IntegerField(write_only=True)
    sucursal_id = serializers.IntegerField(write_only=True, allow_null=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Usuario
        fields = ("id", "email", "nombre", "apellido", "rol", "estado", "is_active", "is_admin",
                  "is_staff", "date_joined", "identificacion", "sucursal", "rol_id", "sucursal_id", "password", "last_login", "is_superuser")
        depth = 1


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ChangePasswordLostSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)

class CotizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotizacion
        fields = ("id", "fecha_creacion", "fecha_vencimiento",
                  "valor_total", "inventario_vehiculos", "vendedor", "cliente")


class OrdenPiezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenPieza
        fields = '__all__'


class PiezasVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiezasVehiculo
        fields = '__all__'


class InventarioPiezaSerializer(serializers.ModelSerializer):
    pieza_id = serializers.IntegerField(write_only=True)
    sucursal_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = InventarioPieza
        fields = ("id", "cantidad_disponible", "pieza",
                  "sucursal", "pieza_id", "sucursal_id")
        depth = 1


class InventarioVehiculoSerializer(serializers.ModelSerializer):
    sucursal_id = serializers.IntegerField(write_only=True)
    vehiculo_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = InventarioVehiculo
        fields = ("id", "modelo", "condicion", "estado", "placa", "kilometraje",
                  "color", "vehiculo", "vehiculo_id", "sucursal", "sucursal_id")
        depth = 1


class OrdenSerializer(serializers.ModelSerializer):
    sucursal_id = serializers.IntegerField(write_only=True)
    cliente_id = serializers.IntegerField(write_only=True)
    vendedor_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Orden
        fields = ("id", "fecha_creacion", "fecha_finalizacion", "tipo", "placa", "valor_mano_obra",
                  "valor_total", "estado", "descripcion", "sucursal", "sucursal_id", "vendedor", "vendedor_id", "cliente", "cliente_id")
        depth = 1


class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        # fields = ("id", "fecha_creacion", "estado", "valor_total",
        #           "inventario_vehiculo", "cotizacion", "vendedor", "cliente")
        fields = '__all__'


class VentaSerializerDetailed(serializers.ModelSerializer):
    inventario_vehiculo = InventarioVehiculoSerializer()

    class Meta:
        model = Venta
        # fields = ("id", "fecha_creacion", "estado", "valor_total",
        #           "inventario_vehiculo", "cotizacion", "vendedor", "cliente")
        fields = '__all__'


class CotizacionSerializerDetailed(serializers.ModelSerializer):
    inventario_vehiculos = InventarioVehiculoSerializer()
    cliente = UsuarioSerializer()

    class Meta:
        model = Cotizacion
        # fields = ("id", "fecha_creacion", "estado", "valor_total",
        #           "inventario_vehiculo", "cotizacion", "vendedor", "cliente")
        fields = '__all__'
