# context_processors.py
from clases.forms import BuscarClaseGeneralForm
from usuarios.forms import BuscarClienteGeneralForm


def add_form_to_context(request):
    return {
        "form_general": BuscarClaseGeneralForm(),
        "form_usuarios": BuscarClienteGeneralForm(request.GET or None),
    }
