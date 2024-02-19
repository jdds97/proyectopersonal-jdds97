from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from fitness.models import Rutina
from clases.models import Clase


class Usuario(AbstractUser):
    """
    Modelo para representar un usuario.
    """

    imagen = models.ImageField(upload_to="usuarios", blank=True, null=True)
    clases_asignadas = models.ManyToManyField(
        Clase, related_name="clases_asignadas", blank=True
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=("groups"),
        blank=True,
        help_text=(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="usuario_groups",
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=("user permissions"),
        blank=True,
        help_text=("Specific permissions for this user."),
        related_name="usuario_user_permissions",
        related_query_name="user",
    )

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name_plural = "Usuarios"
        verbose_name = "Usuario"


class Cliente(Usuario):
    usuario_ptr = models.OneToOneField(
        Usuario, on_delete=models.CASCADE, parent_link=True, default=None
    )
    rutina_asignada = models.ForeignKey(
        Rutina, on_delete=models.SET_NULL, null=True, blank=True
    )
    clases_apuntadas = models.ManyToManyField(
        "clases.Clase", related_name="clientes", blank=True
    )

    fecha_baja = models.DateField(blank=True, null=True)
    ESTADO_CHOICES = [
        ("Activa", "Activa"),
        ("Inactiva", "Inactiva"),
        ("Suspendida", "Suspendida"),
    ]

    estado_membresia = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default="Activa",
    )
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.username)

    def is_client(self):
        return True

    class Meta:
        verbose_name_plural = "Clientes"
        verbose_name = "Cliente"
