"""
Sitio de administración
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Clase, Reserva, TipoClase


admin.site.register(Clase)
admin.site.register(TipoClase)
admin.site.register(Reserva)
