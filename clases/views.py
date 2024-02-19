"""
Vistas de la app clases.
"""

# importa request
from django.utils import timezone
from django.http import HttpRequest, HttpResponse
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.contrib import messages
from django.urls import reverse_lazy


from .models import Clase, Reserva, TipoClase
from .forms import (
    BuscarReservaParaClientesForm,
    CrearClaseForm,
    BuscarClaseForm,
    BuscarClaseGeneralForm,
    BuscarReservaPorClienteForm,
    CrearReservaStaffForm,
)


# pylint: disable=no-member
# region welcome
def welcome(request):
    """
    Vista para la página de bienvenida.
    """
    form_general = BuscarClaseGeneralForm()
    return render(request, "clases/index.html", {"form_general": form_general})


# endregion


# region CRUD de Clases
class CrearClase(CreateView):
    """
    Vista para crear una clase.
    """

    model = Clase
    success_url = reverse_lazy("listar_clases")
    form_class = CrearClaseForm


class ListarClases(ListView):
    """
    Vista para listar las clases.
    """

    model = Clase
    queryset = Clase.objects.filter(
        fecha_clase__gte=timezone.now() + timezone.timedelta(hours=4)
    ).order_by("fecha_clase")
    form_class = BuscarClaseForm
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form_filtros = self.form_class(self.request.GET or None)
        context["form_filtros"] = form_filtros
        context["clases_antiguas"] = Clase.objects.filter(
            fecha_clase__lt=timezone.now()
        ).order_by("fecha_clase")
        form_general = BuscarClaseGeneralForm(self.request.GET or None)
        if form_general.is_valid():
            tipo_clase_general = form_general.cleaned_data["tipo_clase"]
            if tipo_clase_general:
                context["clases_buscadas"] = Clase.objects.filter(
                    tipo_clase__nombre__icontains=tipo_clase_general
                )
                if not context["clases_buscadas"]:
                    messages.warning(self.request, "No se encontraron clases")

        return context

    def get_queryset(self):

        form_filtros = self.form_class(self.request.GET or None)
        if form_filtros.is_valid():
            tramo = form_filtros.cleaned_data["tramo"]
            tipo_clase = form_filtros.cleaned_data["tipo_clase"]
            fecha_clase = form_filtros.cleaned_data["fecha_clase"]
            if tramo:
                self.queryset = self.queryset.filter(tramo=tramo)
            if tipo_clase:
                self.queryset = self.queryset.filter(tipo_clase__nombre=tipo_clase)
            if fecha_clase:
                self.queryset = self.queryset.filter(fecha_clase=fecha_clase)

        return super().get_queryset()


class EditarClase(UpdateView):
    """
    Vista para editar una clase.
    """

    model = Clase
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("listar_clases")
    form_class = CrearClaseForm


class EliminarClase(DeleteView):
    """
    Vista para eliminar una clase.
    """

    model = Clase
    success_url = reverse_lazy("listar_clases")


class DetalleClase(DetailView):
    """
    Vista para ver los detalles de una clase.
    """

    model = Clase


# endregion
# region Clases Adicionales


class TopTenClases(ListView):
    """
    Vista para listar las clases por tipo,tramo o fecha.
    """

    model = Clase
    template_name_suffix = "_top_ten"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clases = (
            Clase.objects.annotate(num_reservas=Count("reserva"))
            .filter(fecha_clase__gte=timezone.now() - timezone.timedelta(days=7))
            .order_by("-num_reservas")[:10]
        )
        context["clases_top_ten"] = clases

        return context


# endregion


# region CRUD de Reservas
class CrearReserva(View):
    """
    Vista para crear una reserva.
    """

    def get(self, request: HttpRequest, pk) -> HttpResponse:
        """
        Método get para obtener una reserva.
        """
        clase = get_object_or_404(Clase, pk=pk)
        if clase.cupos_disponibles == 0:
            messages.warning(request, "No hay cupos disponibles")
            return redirect("listar_clases")
        if Reserva.objects.filter(clase__valido=True, usuario=request.user).exists():
            messages.warning(request, "Ya existe una reserva para este usuario")
            return redirect("listar_clases")
        form_general = BuscarClaseGeneralForm()
        return render(
            request,
            "clases/reserva_form.html",
            {"clase": clase, "form_general": form_general},
        )

    def post(self, request: HttpRequest, pk) -> HttpResponse:
        """
        Método post para crear una reserva.
        """
        clase = get_object_or_404(Clase, pk=pk)
        usuario = request.user
        reserva = Reserva.objects.create(
            clase=clase,
            usuario=usuario,
            estado="Realizada",
            nombre_clase=clase.tipo_clase.nombre,
        )
        clase.valido = True
        clase.cupos_disponibles -= 1
        clase.save()
        messages.success(request, "Reserva realizada")
        return redirect("detalle_reserva", pk=reserva.pk)


class ListarReservas(ListView):
    """
    Vista para listar las reservas.
    """

    model = Reserva
    queryset = Reserva.objects.all()
    form_class = BuscarReservaPorClienteForm
    paginate_by = 2

    def get_queryset(self):
        form = self.form_class(self.request.GET or None)
        if form.is_valid():
            usuario = form.cleaned_data["usuario"]
            clase = form.cleaned_data["clase"]
            if usuario:
                self.queryset = self.queryset.filter(usuario=usuario)
            if clase:
                self.queryset = self.queryset.filter(clase=clase)
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filtros"] = self.form_class(self.request.GET or None)
        return context


class EditarReserva(UpdateView):
    """
    Vista para editar una reserva.
    """

    model = Reserva
    form_class = CrearReservaStaffForm
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("listar_reservas")


class EliminarReserva(DeleteView):
    """
    Vista para eliminar una reserva.
    """

    model = Reserva
    success_url = reverse_lazy("listar_reservas")


class DetalleReserva(DetailView):
    """
    Vista para ver los detalles de una reserva.
    """

    model = Reserva


class CancelarReserva(View):
    """
    Vista para cancelar una reserva.
    """

    def get(self, request, pk) -> HttpResponse:
        """
        Método get para obtener una reserva.
        """
        reserva = get_object_or_404(Reserva, pk=pk)
        return render(
            request, "clases/reserva_confirm_cancel.html", {"reserva": reserva}
        )

    def post(self, request, pk=None, *args, **kwargs) -> HttpResponse:
        """
        Método para cancelar una reserva.
        """
        pk = self.kwargs.get("pk")
        reserva = get_object_or_404(Reserva, pk=pk)
        reserva.estado = "Cancelada"

        if reserva.clase.fecha_clase and reserva.clase.fecha_clase < timezone.now():
            reserva.clase.cupos_disponibles += 1
        reserva.cancelar()
        messages.success(request, "Reserva cancelada")
        if request.user.is_staff:
            return redirect("listar_reservas")
        return redirect("reservas_cliente", request.user.username, request.user.pk)


# endregion
# region Reservas Adicionales
class CrearReservaStaff(View):
    """
    Vista para crear una reserva por el staff.
    """

    def get(self, request, pk):
        """
        Método get para obtener una reserva.
        """
        clase = get_object_or_404(Clase, pk=pk)
        form = CrearReservaStaffForm(initial={"clase": clase})
        return render(request, "clases/reserva_form_staff.html", {"form": form})

    def post(self, request, pk):
        """
        Método post para crear una reserva.
        """
        form = CrearReservaStaffForm(request.POST)
        if form.is_valid():
            clase = get_object_or_404(Clase, pk=pk)
            usuario = form.cleaned_data["usuario"]
            estado = form.cleaned_data["estado"]
            if clase.cupos_disponibles == 0:
                messages.warning(request, "No hay cupos disponibles")
                return redirect("listar_clases")
            if Reserva.objects.filter(clase=clase, usuario=usuario).exists():
                messages.warning(request, "Ya existe una reserva para este usuario")
                return redirect("listar_clases")
            reserva = Reserva.objects.create(
                clase=clase, usuario=usuario, estado=estado
            )
            reserva.save()
            return redirect("listar_reservas")
        return render(request, "clases/reserva_form_staff.html", {"form": form})


class ListarReservasClientes(ListView):
    """
    Vista para listar las clases para los clientes.
    """

    model = Reserva
    template_name_suffix = "_cliente_list"
    form_class = BuscarReservaParaClientesForm
    queryset = None
    paginate_by = 2

    def get_queryset(self):
        self.queryset = Reserva.objects.filter(
            usuario=self.request.user,
            estado="Realizada",
            clase__valido=True,
            clase__fecha_clase=timezone.now(),
        )
        form = self.form_class(self.request.GET or None)
        if form.is_valid():
            fecha = form.cleaned_data["fecha_reserva"]
            clase = form.cleaned_data["clase"]
            if fecha:
                self.queryset = self.queryset.filter(clase__fecha_clase=fecha)
            if clase:
                self.queryset = self.queryset.filter(clase=clase)

        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class(self.request.GET or None)
        return context


# endregion
