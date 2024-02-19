"""
Sitio de administración
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Cliente


class ClienteUserAdmin(UserAdmin):
    model = Usuario
    fieldsets = UserAdmin.fieldsets + (
        (
            "Campos adicionales",
            {
                "fields": (
                    # Campos de Cliente
                    "rutina_asignada",
                    "clases_apuntadas",
                    "fecha_baja",
                    "estado_membresia",
                )
            },
        ),
    )


class CustomUserAdmin(UserAdmin):
    model = Usuario
    fieldsets = UserAdmin.fieldsets + (
        (
            "Campos adicionales",
            {
                "fields": (
                    # Campos de Instructor
                    "clases_asignadas",
                )
            },
        ),
    )


admin.site.register(Usuario, CustomUserAdmin)
admin.site.register(Cliente, ClienteUserAdmin)
