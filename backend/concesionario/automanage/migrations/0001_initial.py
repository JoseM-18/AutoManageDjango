# Generated by Django 4.2.4 on 2023-09-25 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('id_vehiculo', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(blank=True, max_length=255, null=True)),
                ('linea', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo', models.CharField(blank=True, max_length=180, null=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'vehiculos',
                'managed': False,
            },
        ),
    ]
