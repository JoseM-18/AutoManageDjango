from rest_framework import serializers
from .models import Vehiculo, Sucursal, Pieza, Usuario, Rol, Cotizacion, OrdenPieza, PiezasVehiculo, InventarioPieza, InventarioVehiculo, Orden, Venta


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
