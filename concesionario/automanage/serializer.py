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
    class Meta:
        model = Usuario
        fields = '__all__'
        read_only_fields = ('email',)

    def create(self, validated_data):
        user = Usuario.objects.create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class CotizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotizacion
        fields = '__all__'


class OrdenPiezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenPieza
        fields = '__all__'


class PiezasVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiezasVehiculo
        fields = '__all__'


class InventarioPiezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventarioPieza
        fields = '__all__'


class InventarioVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventarioVehiculo
        fields = '__all__'


class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'


class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'
