from django.db import models
from apps.afiliacion.models import *

# Create your models here.
class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Tipo_sancion(TimeStampModel):
    nombre_sancion = models.CharField(help_text='Nombre de la sanción', verbose_name='Nombre sanción', max_length=50)
    duracion_sancion = models.IntegerField(help_text='Cantidad de días que dura la sanción', verbose_name='Duración sanción')

    def __str__(self):
        return self.nombre_sancion + self.duracion_sancion
    class Meta:
        verbose_name = 'Tipo de sanción'
        verbose_name_plural = 'Tipos de sanción'

class Sancion_cliente(TimeStampModel):
    afiliacion_servicio_sancion_cliente = models.ForeignKey(Afiliacion_servicio, help_text='Afiliación servicio a la que se aplica la sanción', verbose_name='Sanción cliente', on_delete=False)
    tipo_sancion = models.ForeignKey(Tipo_sancion, help_text='Tipo de sanción que se va a aplicar', verbose_name='Tipo de sanción', on_delete=False)
    descripcion_sancion_cliente = models.TextField(help_text='Descripción de la sanción', verbose_name='Descripción de la sanción')

    def __str__(self):
        self.afiliacion_servicio_sancion_cliente + self.tipo_sancion + self.created



    class Meta:
        verbose_name = 'Sanción cliente'
        verbose_name_plural = 'Sanciones cliente'

