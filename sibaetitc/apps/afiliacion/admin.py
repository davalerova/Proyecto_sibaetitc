from django.contrib import admin


# Register your models here.
from apps.Servicios.models import *
from apps.cliente.models import *
from .models import *

@admin.register(Tipo_afiliacion)
class Tipo_afiliacionAdmin(admin.ModelAdmin):
    list_display = ('nombre_tipo_afiliacion', 'valor_porcentaje_descuento')

@admin.register(Afiliacion_servicio)
class Afiliacion_servicioAdmin(admin.ModelAdmin):
    list_display = ('cliente_afiliacion', 'servicio_afiliacion', 'tipo_afiliacion', 'afiliacion_activa', 'afiliacion_lunes',
                    'afiliacion_martes', 'afiliacion_miercoles', 'afiliacion_jueves', 'afiliacion_viernes',
                    'afiliacion_sabado', 'fallas_mensuales_afiliacion', 'fallas_acumuladas_afiliacion')