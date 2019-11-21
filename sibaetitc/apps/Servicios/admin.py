from django.contrib import admin

# Register your models here.
from apps.Servicios.models import *

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre_servicio', 'valor_servicio', 'servicio_lunes', 'servicio_martes', 'servicio_miercoles', 'servicio_jueves', 'servicio_viernes', 'servicio_sabado')

@admin.register(Registro_servicio)
class Registro_servicioAdmin(admin.ModelAdmin):
    list_display = ('servicio', 'fecha_servicio', 'servicio_cancelado')