from rest_framework import viewsets, permissions
from clases.models import Clase, Reserva
from usuarios.models import Usuario, Cliente
from .serializers import (
    ClaseSerializer,
    ReservaSerializer,
    UsuarioSerializer,
    ClienteSerializer,
)


# pylint: disable=no-member
class ClaseViewSet(viewsets.ModelViewSet):
    """
    Viewset para Clase model.
    """

    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReservaViewSet(viewsets.ModelViewSet):
    """
    Viewset para Reserva model.
    """

    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    Viewset para Usuario model.
    """

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ClienteViewSet(viewsets.ModelViewSet):
    """
    Viewset para Cliente model.
    """

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Create your views here.
