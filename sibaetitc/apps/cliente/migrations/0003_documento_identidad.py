# Generated by Django 2.2.7 on 2019-11-21 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20191120_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento_identidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('nombre_documento_identidad', models.CharField(help_text='Nombre del documento de identidad', max_length=50, unique=True, verbose_name='Nombre documentos')),
            ],
            options={
                'verbose_name': 'Documento de identidad',
                'verbose_name_plural': 'Documentos de identidad',
            },
        ),
    ]