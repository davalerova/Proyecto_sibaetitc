# Generated by Django 2.2.7 on 2019-11-21 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_auto_20191120_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('nombre_dependencia', models.CharField(help_text='Nombre de la dependencia a la que pertenece, ej: Sistemas, Vigilancia', max_length=50, unique=True, verbose_name='Nombre dependencia')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='tipo_cliente',
            options={'verbose_name': 'Tipos de cliente'},
        ),
        migrations.AlterField(
            model_name='tipo_cliente',
            name='nombre_tipo_cliente',
            field=models.CharField(help_text='Nombre del tipo de cliente, ej: Estudiante Bachillerato', max_length=50, unique=True, verbose_name='nombre tipo cliente'),
        ),
    ]