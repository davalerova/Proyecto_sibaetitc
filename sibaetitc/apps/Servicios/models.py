from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Servicio(TimeStampModel):
    nombre_servicio = models.CharField(help_text='Nombre del servicio de alimentación', verbose_name='Nombre del servicio', max_length=50)
    hora_inicio = models.TimeField(help_text='Hora en que comienza la entrega del servicio', verbose_name='Hora inicio entrega')
    hora_fin = models.TimeField(help_text='Hora en que finaliza la entrega del servicio', verbose_name='Hora finalización entrega')
    valor_servicio = models.PositiveIntegerField(help_text='Valor en pesos colombianos que se debe cancelar por el servicio', verbose_name='Valor servicio')
    servicio_lunes = models.BooleanField(default=True)
    servicio_martes = models.BooleanField(default=True)
    servicio_miercoles = models.BooleanField(default=True)
    servicio_jueves = models.BooleanField(default=True)
    servicio_viernes = models.BooleanField(default=True)
    servicio_sabado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_servicio

class Registro_servicio(TimeStampModel):
    servicio = models.ForeignKey(Servicio, help_text='Servicio que se va a registrar', verbose_name='Servicio', on_delete=False)
    fecha_servicio = models.DateField(help_text='Fecha del servicio', verbose_name='Fecha del servicio')
    servicio_cancelado = models.BooleanField(help_text='True si se cancela el servicio', verbose_name='Servicio cancelado', default=False)

    class Meta:
        verbose_name = 'Registro servicio'
        verbose_name_plural = 'Registro de servicios'