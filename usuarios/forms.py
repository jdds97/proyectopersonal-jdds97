"""
Formularios para el módulo de usuarios.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from clases.models import Clase
from .models import Cliente


# pylint: disable=no-member
class ClienteRegistroForm(UserCreationForm):
    """
    Formulario para el registro de un cliente.
    """

    username = forms.CharField(
        label="Nombre de Usuario",
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre de Usuario"}
        ),
    )
    email = forms.EmailField(
        label="Correo Electrónico",
        max_length=254,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Correo Electrónico"}
        ),
    )
    clases_apuntadas = forms.ModelMultipleChoiceField(
        label="Clases Apuntadas",
        queryset=Clase.objects.all(),
        required=False,  # No requerido
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )

    class Meta:
        """
        Clase meta para el formulario de registro de un cliente.
        """

        model = Cliente
        fields = ("username", "email", "rutina_asignada", "clases_apuntadas")


class EditarClienteForm(forms.ModelForm):
    """
    Formulario para la edición de un cliente.
    """

    model = Cliente

    class Meta:
        """
        Clase meta para el formulario de edición de un cliente.
        """

        model = Cliente
        fields = (
            "first_name",
            "last_name",
            "email",
            "imagen",
            "fecha_nacimiento",
            "rutina_asignada",
            "clases_apuntadas",
            "estado_membresia",
        )
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "imagen": forms.FileInput(attrs={"class": "form-control"}),
            "fecha_nacimiento": forms.DateInput(attrs={"class": "form-control"}),
            "rutina_asignada": forms.Select(attrs={"class": "form-control"}),
            "clases_apuntadas": forms.SelectMultiple(attrs={"class": "form-control"}),
            "estado_membresia": forms.Select(attrs={"class": "form-control"}),
        }


class BuscarClienteGeneralForm(forms.Form):
    """
    Buscar clase general por un solo campo
    """

    username = forms.CharField(
        max_length=150,
        label=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre de Usuario"}
        ),
    )


class BuscarClienteFiltros(forms.Form):
    """
    Formulario para buscar un cliente.
    """

    username = forms.CharField(
        max_length=150,
        label=" Nombre de Usuario",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre de Usuario"}
        ),
    )
    first_name = forms.CharField(
        max_length=150,
        label="Nombre",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre"}
        ),
    )
    last_name = forms.CharField(
        max_length=150,
        label="Apellido",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Apellido"}
        ),
    )
    clases_apuntadas = forms.ModelMultipleChoiceField(
        label="Clases Apuntadas",
        queryset=Clase.objects.all(),
        required=False,  # No requerido
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )
    fecha_baja = forms.DateField(
        label="Fecha de Baja",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )
    estado_membresia = forms.ChoiceField(
        label="Estado de Membresía",
        choices=Cliente.ESTADO_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    fecha_nacimiento = forms.DateField(
        label="Fecha de Nacimiento",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )

    def clean(self):
        """
        Método para validar el formulario.
        """
        cleaned_data = super().clean()
        return cleaned_data
