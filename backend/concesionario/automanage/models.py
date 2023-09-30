from django.db import models


class Cotizacion(models.Model):
    id_cotizacion = models.AutoField(primary_key=True)
    id_inventario_vehiculos = models.ForeignKey(
        'InventarioVehiculo', models.DO_NOTHING, db_column='id_inventario_vehiculos')
    id_vendedor = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='id_vendedor')
    id_cliente = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_cliente',
                                   related_name='cotizaciones_id_cliente_set', blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_vencimiento = models.DateTimeField(blank=True, null=True)
    valor_total = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cotizaciones'


class InventarioPieza(models.Model):
    id_inventario_piezas = models.AutoField(primary_key=True)
    id_pieza = models.ForeignKey(
        'Pieza', models.DO_NOTHING, db_column='id_pieza')
    id_sucursal = models.ForeignKey(
        'Sucursal', models.DO_NOTHING, db_column='id_sucursal')
    cantidad_disponible = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario_piezas'
        unique_together = (('id_pieza', 'id_sucursal'),)


class InventarioVehiculo(models.Model):
    id_inventario_vehiculos = models.AutoField(primary_key=True)
    id_vehiculo = models.ForeignKey(
        'Vehiculo', models.DO_NOTHING, db_column='id_vehiculo', blank=True, null=True)
    id_sucursal = models.ForeignKey(
        'Sucursal', models.DO_NOTHING, db_column='id_sucursal')
    modelo = models.CharField(max_length=10, blank=True, null=True)
    condicion = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    placa = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario_vehiculos'


class OrdenPieza(models.Model):
    id_orden_pieza = models.AutoField(primary_key=True)
    id_orden = models.ForeignKey(
        'Orden', models.DO_NOTHING, db_column='id_orden')
    id_pieza = models.ForeignKey(
        'Pieza', models.DO_NOTHING, db_column='id_pieza')
    cantidad = models.IntegerField(blank=True, null=True)
    valor_total = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden_piezas'
        unique_together = (('id_pieza', 'id_orden'),)


class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    id_sucursal = models.ForeignKey(
        'Sucursal', models.DO_NOTHING, db_column='id_sucursal')
    id_vendedor = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='id_vendedor')
    id_cliente = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='id_cliente', related_name='ordenes_id_cliente_set')
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_finalizacion = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    placa = models.CharField(max_length=10, blank=True, null=True)
    valor_mano_obra = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    valor_total = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordenes'


class Pieza(models.Model):
    id_pieza = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    serie = models.CharField(max_length=80, blank=True, null=True)
    precio = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'piezas'


class PiezasVehiculo(models.Model):
    id_piezas_vehiculo = models.AutoField(primary_key=True)
    id_vehiculo = models.ForeignKey(
        'Vehiculo', models.DO_NOTHING, db_column='id_vehiculo')
    id_pieza = models.ForeignKey(
        Pieza, models.DO_NOTHING, db_column='id_pieza')

    class Meta:
        managed = False
        db_table = 'piezas_vehiculos'
        unique_together = (('id_vehiculo', 'id_pieza'),)


class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sucursales'


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='id_rol')
    nombre = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'


class Vehiculo(models.Model):
    id_vehiculo = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=255, blank=True, null=True)
    linea = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=180, blank=True, null=True)
    precio = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)

    def __str__(self):
        texto = "({0}).{1} - {2}"
        return texto.format(self.id_vehiculo, self.marca, self.linea)

    class Meta:
        managed = False
        db_table = 'vehiculos'


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_inventario_vehiculo = models.IntegerField()
    id_cotizacion = models.ForeignKey(
        Cotizacion, models.DO_NOTHING, db_column='id_cotizacion', blank=True, null=True)
    id_vendedor = models.ForeignKey(
        Usuario, models.DO_NOTHING, db_column='id_vendedor')
    id_cliente = models.ForeignKey(
        Usuario, models.DO_NOTHING, db_column='id_cliente', related_name='ventas_id_cliente_set')
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    valor_total = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas'
