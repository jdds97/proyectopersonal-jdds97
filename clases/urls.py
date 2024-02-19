"""
URLs de la aplicación clases.
"""

from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .views import (
    CrearClase,
    ListarClases,
    EditarClase,
    DetalleClase,
    EliminarClase,
    TopTenClases,
    CrearReserva,
    CrearReservaStaff,
    ListarReservas,
    EditarReserva,
    DetalleReserva,
    EliminarReserva,
    CancelarReserva,
    ListarReservasClientes,
    welcome,
)

urlpatterns = [
    # region welcome
    path("", welcome, name="welcome"),
    # region CRUD de Clases
    path(
        "nuevo/",
        staff_member_required((CrearClase.as_view())),
        name="crear_clase",
    ),
    path(
        "listado/",
        ListarClases.as_view(),
        name="listar_clases",
    ),
    path(
        "editar/<int:pk>",
        staff_member_required((EditarClase.as_view())),
        name="editar_clase",
    ),
    path(
        "eliminar/<int:pk>",
        staff_member_required((EliminarClase.as_view())),
        name="eliminar_clase",
    ),
    path(
        "detalle/<int:pk>",
        DetalleClase.as_view(),
        name="detalle_clase",
    ),
    # region Clase adicional
    path(
        "buscar_general/",
        ListarClases.as_view(),
        name="buscar_clase_general",
    ),
    path(
        "topten/",
        staff_member_required((TopTenClases.as_view())),
        name="top_ten_clases",
    ),
    # endregion
    # region CRUD de Reserva
    path(
        "reserva/nuevo/clase/<int:pk>",
        login_required(CrearReserva.as_view()),
        name="reservar_clase",
    ),
    path(
        "reserva/nuevo/clase/staff/<int:pk>",
        login_required(CrearReservaStaff.as_view()),
        name="reservar_clase_staff",
    ),
    path(
        "reserva/listado/",
        staff_member_required((ListarReservas.as_view())),
        name="listar_reservas",
    ),
    path(
        "reserva/editar/<int:pk>",
        staff_member_required((EditarReserva.as_view())),
        name="editar_reserva",
    ),
    path(
        "reserva/eliminar/<int:pk>",
        staff_member_required((EliminarReserva.as_view())),
        name="eliminar_reserva",
    ),
    path(
        "reserva/detalle/<int:pk>",
        login_required(DetalleReserva.as_view()),
        name="detalle_reserva",
    ),
    path(
        "reserva/cancelar/<int:pk>",
        login_required((CancelarReserva.as_view())),
        name="cancelar_reserva",
    ),
    # endregion
    # region Reserva
    path(
        "reserva/<str:username>/<int:pk>/listado/",
        login_required(ListarReservasClientes.as_view()),
        name="reservas_cliente",
    ),
    # endregion
]
