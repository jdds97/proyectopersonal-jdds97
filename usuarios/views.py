from django.utils import timezone
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse, reverse_lazy
from django.db.models import Count, Max
from .models import Cliente
from django.db.models import Q
from .forms import (
    ClienteRegistroForm,
    EditarClienteForm,
    BuscarClienteFiltros,
    BuscarClienteGeneralForm,
)


# region welcome
def welcome(request):
    """
    Vista para la página de bienvenida.
    """
    return render(request, "usuarios/index.html", {})


# endregion


# region Cliente Registro
class ClienteRegistroView(CreateView):
    """
    Vista para el registro de un cliente.
    """

    model = Cliente
    form_class = ClienteRegistroForm
    success_url = reverse_lazy("login")


# endregion


# region  Cliente Adicional
class MiPerfil(DetailView):
    """
    Vista para el perfil de un cliente.
    """

    model = Cliente
    template_name_suffix = "_perfil"


class EditarCliente(UpdateView):
    """
    Vista para el perfil de un cliente.
    """

    model = Cliente
    template_name_suffix = "_update_form"
    form_class = EditarClienteForm

    def get_success_url(self):
        return reverse(
            "mi_perfil", kwargs={"username": self.object.username, "pk": self.object.pk}
        )


class EliminarCliente(DeleteView):
    """
    Vista para eliminar un cliente.
    """

    model = Cliente
    template_name_suffix = "_confirm_delete"
    success_url = reverse_lazy("listar_clientes")


class ListarClientes(ListView):
    """
    Vista para listar los clientes.
    """

    model = Cliente
    queryset = Cliente.objects.all().order_by("-date_joined")
    form_class = BuscarClienteFiltros
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form_filtros = self.form_class(self.request.GET or None)
        context["form_filtros"] = form_filtros
        context["clientes_antiguos"] = Cliente.objects.filter(
            fecha_baja__lt=timezone.now()
        ).order_by("-fecha_baja")
        form_general = BuscarClienteGeneralForm(self.request.GET or None)
        if form_general.is_valid():
            nombre_usuario_general = form_general.cleaned_data["username"]
            if nombre_usuario_general:
                context["clientes_buscados"] = self.queryset.filter(
                    Q(username__icontains=nombre_usuario_general)
                    | Q(first_name__icontains=nombre_usuario_general)
                    | Q(last_name__icontains=nombre_usuario_general)
                )

        return context


class CancelarMembresia(UpdateView):
    """
    Vista para cancelar la membresia de un cliente.
    """

    model = Cliente
    fields = ["estado_membresia"]
    template_name_suffix = "_confirm_cancel_membresia"
    success_url = reverse_lazy("welcome")

    def get_initial(self):
        return {"estado_membresia": "Inactiva"}


class TopTenClientes(ListView):
    """
    Vista para listar las clases por tipo,tramo o fecha.
    """

    model = Cliente
    template_name_suffix = "_top_ten"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clientes = (
            Cliente.objects.filter(reserva__estado="Realizada")
            .annotate(num_reservas=Count("reserva"))
            .annotate(clase_mas_visitada=Max("reserva__clase__tipo_clase__nombre"))
        ).order_by("-num_reservas")[:10]
        # Cuenta el número de reservas REALIZADAS de los mejores clientes
        context["mejores_clientes"] = clientes
        return context


# endregion
