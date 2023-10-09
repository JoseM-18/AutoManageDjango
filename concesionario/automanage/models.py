from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
# from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, rol, nombre, email, password=None):
        if not email:
            raise ValueError("Usuarios deben contener un email")
        user = self.model(
            email=self.normalize_email(email),
            password=password,
            nombre=nombre,
            rol=Rol(id=rol)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,  rol, nombre, email, password):
        user = self.model(
            email=self.normalize_email(email),
            password=password,
            nombre=nombre,
            rol=Rol(id=rol)
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Rol(models.Model):
    nombre = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'roles'


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True, max_length=255, blank=False, null=False,)
    nombre = models.CharField(max_length=150, blank=True)
    apellido = models.CharField(max_length=150, blank=True)
    rol = models.ForeignKey(Rol, models.DO_NOTHING,
                            db_column='id_rol', blank=True, null=True)
    estado = models.CharField(max_length=25, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now, blank=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["rol", "nombre"]

    objects = UserManager()

    def __str__(self):
        return self.email + " , " + self.nombre

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        managed = True
        db_table = 'usuarios'


class Vehiculo(models.Model):
    marca = models.CharField(max_length=255, blank=True, null=True)
    linea = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=180, blank=True, null=True)
    precio = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)

    def __str__(self):
        texto = "{0}- {1}"
        return texto.format(self.marca, self.linea)

    class Meta:
        managed = True
        db_table = 'vehiculos'


class Sucursal(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sucursales'


class InventarioVehiculo(models.Model):
    vehiculo = models.ForeignKey(
        Vehiculo, models.DO_NOTHING, db_column='id_vehiculo', blank=True, null=True)
    sucursal = models.ForeignKey(
        Sucursal, models.DO_NOTHING, db_column='id_sucursal')
    modelo = models.CharField(max_length=10, blank=True, null=True)
    condicion = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    placa = models.CharField(max_length=10, blank=True, null=True)
    kilometraje = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inventario_vehiculos'


class Cotizacion(models.Model):
    inventario_vehiculos = models.ForeignKey(
        InventarioVehiculo, models.DO_NOTHING, db_column='id_inventario_vehiculos')
    vendedor = models.ForeignKey(
        Usuario, models.DO_NOTHING, db_column='id_vendedor')
    cliente = models.ForeignKey(
        Usuario, models.DO_NOTHING, db_column='id_cliente', related_name='cotizacion_id_cliente_set', blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_vencimiento = models.DateTimeField(blank=True, null=True)
    valor_total = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cotizaciones'


class InventarioPieza(models.Model):
    pieza = models.ForeignKey(
        'Pieza', models.DO_NOTHING, db_column='id_pieza')
    sucursal = models.ForeignKey(
        'Sucursal', models.DO_NOTHING, db_column='id_sucursal')
    cantidad_disponible = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inventario_piezas'
        unique_together = (('pieza', 'sucursal'),)


class OrdenPieza(models.Model):
    orden = models.ForeignKey(
        'Orden', models.DO_NOTHING, db_column='id_orden')
    pieza = models.ForeignKey(
        'Pieza', models.DO_NOTHING, db_column='id_pieza')
    cantidad = models.IntegerField(blank=True, null=True)
    valor_total = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'orden_piezas'
        unique_together = (('orden', 'pieza'),)


class Orden(models.Model):
    sucursal = models.ForeignKey(
        'Sucursal', models.DO_NOTHING, db_column='id_sucursal')
    vendedor = models.ForeignKey(
        Usuario, models.DO_NOTHING, db_column='id_vendedor')
    cliente = models.ForeignKey(
        Usuario, models.DO_NOTHING, db_column='id_cliente', related_name='ordenes_id_cliente_set')
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_finalizacion = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    placa = models.CharField(max_length=10, blank=True, null=True)
    valor_mano_obra = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    valor_total = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)
    estado = models.CharField(max_length=150, blank=True, null=False)

    class Meta:
        managed = True
        db_table = 'ordenes'


class Pieza(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    serie = models.CharField(max_length=80, blank=True, null=True)
    precio = models.DecimalField(
        max_digits=19, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'piezas'


class PiezasVehiculo(models.Model):
    vehiculo = models.ForeignKey(
        'Vehiculo', models.DO_NOTHING, db_column='id_vehiculo')
    pieza = models.ForeignKey(
        Pieza, models.DO_NOTHING, db_column='id_pieza')

    class Meta:
        managed = True
        db_table = 'piezas_vehiculos'
        unique_together = (('vehiculo', 'pieza'),)


class Venta(models.Model):
    inventario_vehiculo = models.ForeignKey(
        InventarioVehiculo, models.DO_NOTHING, db_column='id_inventario_vehiculos')
    cotizacion = models.ForeignKey(
        Cotizacion, models.DO_NOTHING, db_column='id_cotizacion', blank=True, null=True)
    vendedor = models.ForeignKey(
        Usuario, models.DO_NOTHING, db_column='id_vendedor')
    cliente = models.ForeignKey(
        Usuario, models.DO_NOTHING, db_column='id_cliente', related_name='ventas_id_cliente_set')
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    valor_total = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ventas'
