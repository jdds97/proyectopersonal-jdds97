"""
Formularios para la app clases
"""

from django import forms
from usuarios.models import Cliente, Usuario
from .models import Clase, Reserva, TipoClase


# pylint: disable=no-member
# region Formularios  de Clases
# Crea un formulario para crear una clase
class CrearClaseForm(forms.ModelForm):
    """
    Formulario para crear una clase.
    """

    class Meta:
        """
        Meta clase para el formulario.
        """

        model = Clase
        fields = "__all__"
        widgets = {
            "tipo_clase": forms.Select(attrs={"class": "form-control"}),
            "tramo": forms.Select(attrs={"class": "form-control"}),
            "fecha_clase": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"},
            ),
            "usuarios": forms.SelectMultiple(
                attrs={"class": "form-control"}
            ),  # Se corrigió el nombre del campo a "usuarios"
            "cupos_disponibles": forms.NumberInput(attrs={"class": "form-control"}),
            "instructor": forms.Select(attrs={"class": "form-control"}),
            "imagen": forms.FileInput(attrs={"class": "form-control"}),
        }
        labels = {
            "tramo": "Tramo en minutos",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.initial["fecha_clase"] = self.instance.fecha_clase.strftime(
                "%Y-%m-%dT%H:%M"
            )
        self.fields["instructor"].queryset = Usuario.objects.filter(is_staff=True)


class CrearReservaStaffForm(forms.ModelForm):
    """
    Formulario para crear una reserva.
    """

    class Meta:
        """
        Meta clase para el formulario.
        """

        model = Reserva
        fields = ["usuario", "estado"]
        widgets = {
            "usuario": forms.Select(attrs={"class": "form-control"}),
            "estado": forms.Select(attrs={"class": "form-control"}),
        }


class BuscarClaseGeneralForm(forms.Form):
    """
    Buscar clase general por un solo campo
    """

    tipo_clase = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs={
                "class": "inline-block form-control",
                "role": "search",
                "placeholder": "Busca por el tipo de clase",
            }
        ),
    )


class BuscarClaseForm(forms.Form):
    """
    Formulario para buscar una clase.
    """

    tramo = forms.ChoiceField(
        choices=[
            ("", "----")
        ]  # Campo nulo para que el usuario pueda seleccionar todas las opciones
        + [
            (x, x) for x in range(20, 121, 20)
        ],  # En este código, choices es una lista de tuplas, donde cada tupla contiene un número y su representación en cadena de texto. La lista se genera con una comprensión de lista que recorre los números de 20 en 20 hasta 120.
        # Por ejemplo, en la primera iteración, se generará la tupla (20, '20'). En la segunda iteración, se generará la tupla (40, '40'), y así sucesivamente.
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Tramo en minutos",
    )
    tipo_clase = forms.ModelChoiceField(
        queryset=TipoClase.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Todas las clases",
        required=False,
    )

    fecha_clase = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control",
                "type": "date",
                "placeholder": "Fecha de la clase Vacío para todas las fechas",
            }
        ),
    )

    def clean(self):
        """
        Método para validar el formulario.
        """
        cleaned_data = super().clean()
        return cleaned_data


# endregion


# region Formularios de Reservas
class BuscarReservaPorClienteForm(forms.Form):
    """
    Formulario para buscar una reserva por cliente y un usuario.
    """

    usuario = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
    )

    clase = forms.ModelChoiceField(
        queryset=Clase.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
    )

    def clean(self):
        """
        Método para validar el formulario.
        """
        cleaned_data = super().clean()

        return cleaned_data


class BuscarReservaParaClientesForm(forms.Form):
    """
    Formulario para buscar reservas de un cliente por fecha.
    """

    fecha_reserva = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control",
                "type": "date",
                "placeholder": "Fecha de la clase Vacío para todas las fechas",
            }
        ),
    )
    clase = forms.ModelChoiceField(
        queryset=Clase.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    def __init__(self, *args, **kwargs):
        """
        Inicializa el formulario.

        Args:
            *args: Argumentos posicionales.
            **kwargs: Argumentos con nombre.
        """
        user = kwargs.pop("user", None)
        super(BuscarReservaParaClientesForm, self).__init__(*args, **kwargs)
        if user:
            self.fields["clase"].queryset = Clase.objects.filter(usuario=user)

    def clean(self):
        """
        Método para validar el formulario.
        """
        cleaned_data = super().clean()

        return cleaned_data


# endregion
