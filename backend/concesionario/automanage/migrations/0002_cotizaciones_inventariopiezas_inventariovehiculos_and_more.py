# Generated by Django 4.2.4 on 2023-09-25 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automanage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizaciones',
            fields=[
                ('id_cotizacion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_vencimiento', models.DateTimeField(blank=True, null=True)),
                ('valor_total', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'cotizaciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InventarioPiezas',
            fields=[
                ('id_inventario_piezas', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_disponible', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'inventario_piezas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InventarioVehiculos',
            fields=[
                ('id_inventario_vehiculos', models.AutoField(primary_key=True, serialize=False)),
                ('modelo', models.CharField(blank=True, max_length=10, null=True)),
                ('condicion', models.CharField(blank=True, max_length=50, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('placa', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'inventario_vehiculos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ordenes',
            fields=[
                ('id_orden', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_finalizacion', models.DateTimeField(blank=True, null=True)),
                ('tipo', models.CharField(blank=True, max_length=50, null=True)),
                ('placa', models.CharField(blank=True, max_length=10, null=True)),
                ('valor_mano_obra', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('valor_total', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'ordenes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Piezas',
            fields=[
                ('id_pieza', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('serie', models.CharField(blank=True, max_length=80, null=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'piezas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PiezasVehiculos',
            fields=[
                ('id_vehiculo', models.OneToOneField(db_column='id_vehiculo', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='automanage.vehiculos')),
            ],
            options={
                'db_table': 'piezas_vehiculos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'db_table': 'roles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('id_sucursal', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_creacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sucursales',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('estado', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'usuarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('id_inventario_vehiculo', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('valor_total', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'ventas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrdenPiezas',
            fields=[
                ('id_pieza', models.OneToOneField(db_column='id_pieza', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='automanage.piezas')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('valor_total', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'orden_piezas',
                'managed': False,
            },
        ),
    ]
