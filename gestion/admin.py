from django.contrib import admin
from .models import Cliente, Cuenta, Transaccion


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "email",
        "telefono",
        "fecha_registro",
    )
    search_fields = (
        "nombre",
        "email",
    )


@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = (
        "numero",
        "cliente",
        "saldo",
        "moneda",
        "activa",
        "fecha_creacion",
    )
    search_fields = (
        "numero",
        "cliente__nombre",
    )
    list_filter = (
        "moneda",
        "activa",
    )


@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = (
        "cuenta",
        "tipo",
        "monto",
        "descripcion",
        "fecha",
    )
    search_fields = (
        "cuenta__numero",
        "descripcion",
    )
    list_filter = (
        "tipo",
    )