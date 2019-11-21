from django.contrib import admin
from apps.cliente.models import *

# Register your models here.


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre_genero',)

@admin.register(Documento_identidad)
class Documento_identidadAdmin(admin.ModelAdmin):
    list_display = ('nombre_documento_identidad',)

@admin.register(Tipo_cliente)
class Tipo_clienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_tipo_cliente',)

@admin.register(Dependencia)
class DependenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre_dependencia',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_rfid_cliente', 'documento_identidad', 'numero_documento_identidad_cliente', 'nombres_cliente',
                    'apellidos_cliente', 'email_cliente', 'fecha_nacimiento_cliente', 'saldo_cliente', 'genero_cliente',
                    'tipo_cliente', 'dependencia_cliente')