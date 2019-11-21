from django.db import models
from apps.cliente.models import Cliente
from apps.Servicios.models import Servicio

# Create your models here.
class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Tipo_afiliacion(TimeStampModel):
    nombre_tipo_afiliacion = models.CharField(help_text='Nombre del tipo de afiliación', verbose_name='Nombre de afiliación', max_length=50)
    valor_porcentaje_descuento = models.IntegerField(help_text='Valor del porcentaje de descuento', verbose_name='Valor porcentaje de descuento')

    def __str__(self):
        return self.nombre_tipo_afiliacion
    class Meta:
        verbose_name = 'Tipo de afiliación'
        verbose_name_plural = 'Tipos de afiliación'

class Afiliacion_servicio(TimeStampModel):
    cliente_afiliacion = models.ForeignKey(Cliente, help_text='Cliente que se va afiliar', verbose_name='Cliente afiliación', on_delete=False)
    servicio_afiliacion = models.ForeignKey(Servicio, help_text='Servicio al que se va a afiliar el cliente', verbose_name='Servicio afiliación', on_delete=False)
    tipo_afiliacion = models.ForeignKey(Tipo_afiliacion, help_text='Tipo de afiliación del servicio', verbose_name='Tipo de afiliación', on_delete=False)
    afiliacion_activa = models.BooleanField(help_text='La afiliación se encuentra activa', verbose_name='Afiliación activa', default=True)
    afiliacion_lunes = models.BooleanField( default=True )
    afiliacion_martes = models.BooleanField( default=True )
    afiliacion_miercoles = models.BooleanField( default=True )
    afiliacion_jueves = models.BooleanField( default=True )
    afiliacion_viernes = models.BooleanField( default=True )
    afiliacion_sabado = models.BooleanField( default=True )
    fallas_mensuales_afiliacion = models.PositiveIntegerField(help_text='Número de fallas al servicio afiliado del mes actual', verbose_name='Fallas mensuales afiliación')
    fallas_acumuladas_afiliacion = models.PositiveIntegerField(help_text='Número de fallas acumuladas del servicio afiliado', verbose_name='Fallas acumuladas afiliación')

    def __str__(self):
        self.cliente_afiliacion + self.servicio_afiliacion + self.tipo_afiliacion



    class Meta:
        verbose_name = 'Afiliación servicio'
        verbose_name_plural = 'Afiliación servicios'

