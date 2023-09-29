from rest_framework import serializers
from .models import Vehiculo


class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        # fields=('id_vehiculo','marca','linea')
        fields = '__all__'
