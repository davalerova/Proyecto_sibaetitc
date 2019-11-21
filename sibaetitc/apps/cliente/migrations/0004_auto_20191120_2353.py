# Generated by Django 2.2.7 on 2019-11-21 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_documento_identidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('nombre_tipo_cliente', models.CharField(help_text='Nombre del tipo de cliente, ej: Estudiante Bachillerato', max_length=50, unique=True, verbose_name='nombre_tipo_cliente')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='documento_identidad',
            name='nombre_documento_identidad',
            field=models.CharField(help_text='Nombre del documento de identidad', max_length=50, unique=True, verbose_name='Nombre documento'),
        ),
        migrations.AlterField(
            model_name='genero',
            name='nombre_genero',
            field=models.CharField(help_text='Nombre del género', max_length=50, unique=True, verbose_name='Nombre género'),
        ),
    ]