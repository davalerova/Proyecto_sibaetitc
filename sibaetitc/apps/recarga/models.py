from django.db import models
from apps.cliente.models import Cliente

# Create your models here.
class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Recarga(TimeStampModel):
    cliente_recarga = models.ForeignKey(Cliente, help_text='Cliente al que se le realiza la recarga', verbose_name='Cliente recarga', on_delete=False)
    valor_recarga = models.IntegerField(help_text='Valor de la recarga en pesos colombianos', verbose_name='Valor de la recarga')

