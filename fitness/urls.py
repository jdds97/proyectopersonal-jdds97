from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .views import (
    CrearEjercicio,
    ListarEjercicios,
    EditarEjercicio,
    EliminarEjercicio,
    CrearTipoEntrenamiento,
    ListarTipoEntrenamientos,
    EditarTipoEntrenamiento,
    EliminarTipoEntrenamiento,
    CrearRutina,
    ListarRutinas,
    EditarRutina,
    EliminarRutina,
    welcome,
)

urlpatterns = [
    # region welcome
    path("", welcome, name="welcome"),
    # endregion
    # region CRUD de Ejercicios
    path(
        "ejercicio/nuevo/",
        staff_member_required(login_required(CrearEjercicio.as_view())),
        name="crear_ejercicio",
    ),
    path(
        "ejercicio/listado/",
        staff_member_required(login_required(ListarEjercicios.as_view())),
        name="listar_ejercicios",
    ),
    path(
        "ejercicio/editar/<int:pk>",
        staff_member_required(login_required(EditarEjercicio.as_view())),
        name="editar_ejercicio",
    ),
    path(
        "ejercicio/eliminar/<int:pk>",
        staff_member_required(login_required(EliminarEjercicio.as_view())),
        name="eliminar_ejercicio",
    ),
    # endregion
    # region CRUD de Tipo de Entrenamiento
    path(
        "tipo_entrenamiento/nuevo/",
        staff_member_required(login_required(CrearTipoEntrenamiento.as_view())),
        name="crear_tipo_entrenamiento",
    ),
    path(
        "tipo_entrenamiento/listado/",
        staff_member_required(login_required(ListarTipoEntrenamientos.as_view())),
        name="listar_tipo_entrenamientos",
    ),
    path(
        "tipo_entrenamiento/editar/<int:pk>",
        staff_member_required(login_required(EditarTipoEntrenamiento.as_view())),
        name="editar_tipo_entrenamiento",
    ),
    path(
        "tipo_entrenamiento/eliminar/<int:pk>",
        staff_member_required(login_required(EliminarTipoEntrenamiento.as_view())),
        name="eliminar_tipo_entrenamiento",
    ),
    # endregion
    # region CRUD de Rutina
    path(
        "rutina/nuevo/",
        staff_member_required(login_required(CrearRutina.as_view())),
        name="crear_rutina",
    ),
    path(
        "rutina/listado/",
        staff_member_required(login_required(ListarRutinas.as_view())),
        name="listar_rutinas",
    ),
    path(
        "rutina/editar/<int:pk>",
        staff_member_required(login_required(EditarRutina.as_view())),
        name="editar_rutina",
    ),
    path(
        "rutina/eliminar/<int:pk>",
        staff_member_required(login_required(EliminarRutina.as_view())),
        name="eliminar_rutina",
    ),
    # endregion
]
