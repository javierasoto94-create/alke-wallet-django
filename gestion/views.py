from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Cliente, Cuenta, Transaccion
from .forms import ClienteForm, CuentaForm, TransaccionForm


# =========================
# CLIENTES
# =========================

class ClienteListView(ListView):
    model = Cliente
    template_name = "gestion/cliente_list.html"
    context_object_name = "clientes"


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "gestion/cliente_form.html"
    success_url = reverse_lazy("cliente-list")


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "gestion/cliente_form.html"
    success_url = reverse_lazy("cliente-list")


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "gestion/cliente_confirm_delete.html"
    success_url = reverse_lazy("cliente-list")


# =========================
# CUENTAS
# =========================

class CuentaListView(ListView):
    model = Cuenta
    template_name = "gestion/cuenta_list.html"
    context_object_name = "cuentas"


class CuentaCreateView(CreateView):
    model = Cuenta
    form_class = CuentaForm
    template_name = "gestion/cuenta_form.html"
    success_url = reverse_lazy("cuenta-list")


class CuentaUpdateView(UpdateView):
    model = Cuenta
    form_class = CuentaForm
    template_name = "gestion/cuenta_form.html"
    success_url = reverse_lazy("cuenta-list")


class CuentaDeleteView(DeleteView):
    model = Cuenta
    template_name = "gestion/cuenta_confirm_delete.html"
    success_url = reverse_lazy("cuenta-list")


# =========================
# TRANSACCIONES
# =========================

class TransaccionListView(ListView):
    model = Transaccion
    template_name = "gestion/transaccion_list.html"
    context_object_name = "transacciones"


class TransaccionCreateView(CreateView):
    model = Transaccion
    form_class = TransaccionForm
    template_name = "gestion/transaccion_form.html"
    success_url = reverse_lazy("transaccion-list")


class TransaccionUpdateView(UpdateView):
    model = Transaccion
    form_class = TransaccionForm
    template_name = "gestion/transaccion_form.html"
    success_url = reverse_lazy("transaccion-list")


class TransaccionDeleteView(DeleteView):
    model = Transaccion
    template_name = "gestion/transaccion_confirm_delete.html"
    success_url = reverse_lazy("transaccion-list")