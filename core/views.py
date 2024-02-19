"""

"""

from django.shortcuts import render


def welcome(request):
    """
    Vista para la página de bienvenida.
    """
    return render(request, "core/index.html", {})
