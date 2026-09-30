from django import forms
from .models import Cliente, Cuenta, Transaccion


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            "usuario",
            "nombre",
            "email",
            "telefono",
        ]


class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = [
            "cliente",
            "numero",
            "saldo",
            "moneda",
            "activa",
            "beneficiarios",
        ]


class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = [
            "cuenta",
            "tipo",
            "monto",
            "descripcion",
        ]