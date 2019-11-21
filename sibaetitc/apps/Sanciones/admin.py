from django.contrib import admin


# Register your models here.
from apps.afiliacion.models import *
from .models import *

@admin.register(Tipo_sancion)
class Tipo_sancionAdmin(admin.ModelAdmin):
    list_display = ('nombre_sancion', 'duracion_sancion')

@admin.register(Sancion_cliente)
class Sancion_clienteAdmin(admin.ModelAdmin):
    list_display = ('afiliacion_servicio_sancion_cliente', 'tipo_sancion', 'descripcion_sancion_cliente', 'created')