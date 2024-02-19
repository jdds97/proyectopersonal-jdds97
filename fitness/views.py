from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ejercicio, TipoEntrenamiento, Rutina


# region welcome
def welcome(request):
    """
    Vista para la página de bienvenida.
    """
    return render(request, "fitness/index.html", {})


# endregion
# region CRUD de Ejercicios
class CrearEjercicio(CreateView):
    """
    Vista para crear un ejercicio.
    """

    model = Ejercicio
    fields = "__all__"
    success_url = reverse_lazy("listar_ejercicios")


class ListarEjercicios(ListView):
    """
    Vista para listar los ejercicios.
    """

    model = Ejercicio


class EditarEjercicio(UpdateView):
    """
    Vista para editar un ejercicio.
    """

    model = Ejercicio
    fields = "__all__"
    success_url = reverse_lazy("listar_ejercicios")


class EliminarEjercicio(DeleteView):
    """
    Vista para eliminar un ejercicio.
    """

    model = Ejercicio
    success_url = reverse_lazy("listar_ejercicios")


# endregion
# region CRUD de Tipo de Entrenamiento
class CrearTipoEntrenamiento(CreateView):
    """
    Vista para crear un tipo de entrenamiento.
    """

    model = TipoEntrenamiento
    fields = "__all__"
    success_url = reverse_lazy("listar_tipo_entrenamientos")


class ListarTipoEntrenamientos(ListView):
    """
    Vista para listar los tipos de entrenamientos.
    """

    model = TipoEntrenamiento


class EditarTipoEntrenamiento(UpdateView):
    """
    Vista para editar un tipo de entrenamiento.
    """

    model = TipoEntrenamiento
    fields = "__all__"
    success_url = reverse_lazy("listar_tipo_entrenamientos")


class EliminarTipoEntrenamiento(DeleteView):
    """
    Vista para eliminar un tipo de entrenamiento.
    """

    model = TipoEntrenamiento
    success_url = reverse_lazy("listar_tipo_entrenamientos")


# endregion
# region CRUD de Rutina
class CrearRutina(CreateView):
    """
    Vista para crear una rutina.
    """

    model = Rutina
    fields = "__all__"
    success_url = reverse_lazy("listar_rutinas")


class ListarRutinas(ListView):
    """
    Vista para listar las rutinas.
    """

    model = Rutina


class EditarRutina(UpdateView):
    """
    Vista para editar una rutina.
    """

    model = Rutina
    fields = "__all__"
    success_url = reverse_lazy("listar_rutinas")


class EliminarRutina(DeleteView):
    """
    Vista para eliminar una rutina.
    """

    model = Rutina
    success_url = reverse_lazy("listar_rutinas")


# endregion
