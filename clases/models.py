"""
Modelos de clases para la app clases del gimnasio
"""

from django.db import models


class TipoClase(models.Model):
    """
    Modelo para representar un tipo de clase.
    """

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return str(self.nombre)


class Clase(models.Model):
    """
    Modelo para representar una clase.
    """

    tramo = models.PositiveIntegerField(
        default=20, choices=[(i, i) for i in range(20, 121, 20)]
    )
    tipo_clase = models.ForeignKey(
        TipoClase,
        on_delete=models.CASCADE,
    )
    instructor = models.ForeignKey(
        "usuarios.Usuario",
        on_delete=models.CASCADE,
        default=None,
        related_name="instructor",
    )
    cupos_disponibles = models.PositiveIntegerField(default=0)
    usuarios = models.ManyToManyField(
        "usuarios.Cliente", blank=True, related_name="usuarios"
    )
    fecha_clase = models.DateTimeField(null=True, blank=True)
    imagen = models.ImageField(upload_to="clases", blank=True, null=True)
    valido = models.BooleanField(default=True)

    def __str__(self):
        return f"Clase - {self.tipo_clase}"


class Reserva(models.Model):
    """
    Modelo para representar una reserva.
    """

    usuario = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, null=True, blank=True)
    estado_choices = (
        ("Pendiente", "Pendiente"),
        ("Cancelada", "Cancelada"),
        ("Realizada", "Realizada"),
    )
    estado = models.CharField(
        max_length=10, choices=estado_choices, default="Pendiente"
    )
    nombre_clase = models.CharField(max_length=100, default=None)

    def __str__(self):
        return f"Reserva - {self.usuario} - {self.clase} - {self.estado}"

    def cancelar(self):
        self.estado = "Cancelada"
        self.clase.valido = False
        self.nombre_clase = self.clase.tipo_clase.nombre
        self.clase = None
        self.save()
