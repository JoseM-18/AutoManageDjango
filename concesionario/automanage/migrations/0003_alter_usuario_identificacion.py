# Generated by Django 4.2.4 on 2023-10-21 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automanage', '0002_usuario_identificacion_usuario_sucursal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='identificacion',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
