from rest_framework import serializers
from clases.models import Clase, Reserva
from usuarios.models import Usuario, Cliente


class ClaseSerializer(serializers.ModelSerializer):
    """
    Serializer para Clase model.
    """

    class Meta:
        """
        Meta class para ClaseSerializer.
        """

        model = Clase
        fields = "__all__"


class ReservaSerializer(serializers.ModelSerializer):
    """
    Serializer para Reserva model.
    """

    class Meta:
        """
        Meta class para ReservaSerializer.
        """

        model = Reserva
        fields = "__all__"


class UsuarioSerializer(serializers.ModelSerializer):
    """
    Serializer para Usuario model.
    """

    class Meta:
        """
        Meta class para UsuarioSerializer.
        """

        model = Usuario
        fields = "__all__"


class ClienteSerializer(serializers.ModelSerializer):
    """
    Serializer para Cliente model.
    """

    class Meta:
        """
        Meta class para ClienteSerializer.
        """

        model = Cliente
        fields = "__all__"
