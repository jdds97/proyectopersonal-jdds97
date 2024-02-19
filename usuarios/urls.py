from django.urls import include, path
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .views import (
    ClienteRegistroView,
    MiPerfil,
    EditarCliente,
    EliminarCliente,
    ListarClientes,
    CancelarMembresia,
    TopTenClientes,
    welcome,
)


urlpatterns = [
    # region welcome
    path("", welcome, name="welcome"),
    # endregion
    # region inicio sesión de usuario
    path("accounts/", include("django.contrib.auth.urls")),
    # endregion
    # region registro de usuario
    path("registro/", ClienteRegistroView.as_view(), name="registro"),
    # endregion
    # region CRUD Cliente
    path(
        "mi_perfil/<str:username>/<int:pk>/",
        login_required(MiPerfil.as_view()),
        name="mi_perfil",
    ),
    path(
        "mi_perfil/<str:username>/<int:pk>/editar/",
        login_required(EditarCliente.as_view()),
        name="editar_cliente",
    ),
    path(
        "eliminar/<int:pk>/",
        login_required(EliminarCliente.as_view()),
        name="eliminar_cliente",
    ),
    path(
        "mi_perfil/<str:username>/<int:pk>/eliminar/",
        login_required(CancelarMembresia.as_view()),
        name="cancelar_membresia",
    ),
    # endregion
    # region Usuario adicional
    path(
        "listado/",
        staff_member_required(ListarClientes.as_view()),
        name="listar_clientes",
    ),
    path(
        "top_ten/",
        staff_member_required(TopTenClientes.as_view()),
        name="top_ten_clientes",
    ),
    path(
        "buscar_general/",
        staff_member_required(ListarClientes.as_view()),
        name="buscar_cliente_general",
    ),
    # endregion
]
# endregion
