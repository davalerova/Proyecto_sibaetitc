from django.contrib import admin

# Register your models here.
from apps.recarga.models import *

@admin.register(Recarga)
class RecargaAdmin(admin.ModelAdmin):
    list_display = ('cliente_recarga', 'valor_recarga', 'created')