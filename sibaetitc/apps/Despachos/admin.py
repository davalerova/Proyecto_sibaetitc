from django.contrib import admin

# Register your models here.
from apps.afiliacion.models import *
from .models import *

@admin.register(Consumo_Servicio)
class RecargaAdmin(admin.ModelAdmin):
    list_display = ('afiliacion_servicio', 'valor_cancelado_servicio', 'created' )

