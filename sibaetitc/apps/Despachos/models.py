from django.db import models

# Create your models here.
from apps.afiliacion.models import Afiliacion_servicio

class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Consumo_Servicio(TimeStampModel):
    afiliacion_servicio = models.ForeignKey(Afiliacion_servicio, help_text='Servicio afiliado recibido', verbose_name='Servicio afiliado', on_delete=False)
    valor_cancelado_servicio = models.PositiveIntegerField(help_text='Valor cancelado por el cliente por el servicio recibido')

    class Meta:
        verbose_name = 'Consumo de servicios'
        verbose_name_plural = 'Cosumos de servicios'