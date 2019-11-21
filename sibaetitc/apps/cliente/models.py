from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Genero(TimeStampModel):
    nombre_genero = models.CharField(help_text="Nombre del género", max_length=50, unique=True, verbose_name='Nombre género')

    def __str__(self):
        return self.nombre_genero

    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'

class Documento_identidad(TimeStampModel):
    nombre_documento_identidad = models.CharField(help_text='Nombre del documento de identidad', max_length=50, unique=True, verbose_name='Nombre documento')

    def __str__(self):
        return self.nombre_documento_identidad

    class Meta:
        verbose_name = 'Documento de identidad'
        verbose_name_plural = 'Documentos de identidad'

class Tipo_cliente(TimeStampModel):
    nombre_tipo_cliente = models.CharField(help_text='Nombre del tipo de cliente, ej: Estudiante Bachillerato', max_length=50, unique=True, verbose_name='nombre tipo cliente')

    def __str__(self):
        return self.nombre_tipo_cliente

    class Meta:
        verbose_name='Tipos de cliente'

class Dependencia(TimeStampModel):
    nombre_dependencia = models.CharField(help_text='Nombre de la dependencia a la que pertenece, ej: Sistemas, Vigilancia', max_length=50, unique=True, verbose_name='Nombre dependencia')

    def __str__(self):
        return self.nombre_dependencia

class Cliente(TimeStampModel):
    id_rfid_cliente = models.CharField(help_text='Id RFID carné o llavero', max_length=50, unique=True, verbose_name='Id RFID')
    documento_identidad = models.ForeignKey(Documento_identidad, help_text='Documento de identidad del cliente', verbose_name='Documento de identidad', on_delete=False)
    numero_documento_identidad_cliente = models.CharField(help_text='Número del documento de identidad del cliente', unique=True, max_length=15, verbose_name='Número de documento de identidad')
    nombres_cliente = models.CharField(help_text='Nombres del cliente', max_length=50, verbose_name='Nombres')
    apellidos_cliente = models.CharField(help_text='Apellidos del cliente', max_length=50, verbose_name='Apellidos')
    email_cliente = models.EmailField(help_text='Correo electrónico cliente', max_length=70, verbose_name='Correo electrónico')
    fecha_nacimiento_cliente = models.DateField(verbose_name='Fecha de nacimiento')
    saldo_cliente = models.IntegerField(verbose_name='Saldo')
    genero_cliente = models.ForeignKey(Genero, help_text='Gérero del cliente', verbose_name='Género', on_delete=False)
    tipo_cliente = models.ForeignKey(Tipo_cliente, help_text='Tipo de cliente', verbose_name='Tipo', on_delete=False)
    dependencia_cliente = models.ForeignKey(Dependencia, help_text='Dependencia a la que pertenece', verbose_name='Dependencia', on_delete=False)

    def __str__(self):
        return self.nombres_cliente + ' ' + self.apellidos_cliente
