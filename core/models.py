"""
Módulo de modelos de la aplicación core
"""

from django.db import models
from usuarios.models import Usuario, Cliente
from fitness.models import Rutina


class Gimnasio(models.Model):
    """
    Modelo para Gimnasio
    """

    nombre = models.CharField(
        max_length=100, unique=True, help_text="Nombre del gimnasio"
    )
    direccion = models.CharField(max_length=255, help_text="Dirección del gimnasio")
    descripcion = models.TextField(
        blank=True, null=True, help_text="Descripción del gimnasio"
    )
    instructores = models.ManyToManyField(
        Usuario,
        related_name="gimnasios_instructores",
        blank=True,
        help_text="Instructores del gimnasio",
    )

    soporte_fitness = models.ManyToManyField(
        Rutina,
        related_name="gimnasios_soporte_fitness",
        blank=True,
        help_text="Soporte fitness del gimnasio",
    )
    miembros = models.ManyToManyField(
        Cliente,
        related_name="gimnasios_miembros",
        blank=True,
        help_text="Miembros del gimnasio",
    )
    logo = models.ImageField(
        upload_to="gimnasio_logos/",
        blank=True,
        null=True,
        help_text="Logo del gimnasio",
    )
    trabajadores = models.ManyToManyField(
        Usuario,
        related_name="gimnasios_trabajadores",
        blank=True,
        help_text="Trabajadores del gimnasio",
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        """
        Metadatos para el modelo Gimnasio
        """

        verbose_name = "Gimnasio"
        verbose_name_plural = "Gimnasios"
