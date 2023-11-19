from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Vehiculo, Rol, Usuario


class UsuarioAdmin(admin.ModelAdmin):
    ordering = ['email']


admin.site.register(Vehiculo)
admin.site.register(Rol)
admin.site.register(Usuario, UsuarioAdmin)
# Register your models here.
