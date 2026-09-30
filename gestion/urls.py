from django.urls import path

from .views import (
    ClienteListView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView,
    CuentaListView,
    CuentaCreateView,
    CuentaUpdateView,
    CuentaDeleteView,
    TransaccionListView,
    TransaccionCreateView,
    TransaccionUpdateView,
    TransaccionDeleteView,
)


urlpatterns = [
    # Clientes
    path("clientes/", ClienteListView.as_view(), name="cliente-list"),
    path("clientes/nuevo/", ClienteCreateView.as_view(), name="cliente-create"),
    path(
        "clientes/editar/<int:pk>/",
        ClienteUpdateView.as_view(),
        name="cliente-update",
    ),
    path(
        "clientes/eliminar/<int:pk>/",
        ClienteDeleteView.as_view(),
        name="cliente-delete",
    ),

    # Cuentas
    path("cuentas/", CuentaListView.as_view(), name="cuenta-list"),
    path("cuentas/nueva/", CuentaCreateView.as_view(), name="cuenta-create"),
    path(
        "cuentas/editar/<int:pk>/",
        CuentaUpdateView.as_view(),
        name="cuenta-update",
    ),
    path(
        "cuentas/eliminar/<int:pk>/",
        CuentaDeleteView.as_view(),
        name="cuenta-delete",
    ),

    # Transacciones
    path(
        "transacciones/",
        TransaccionListView.as_view(),
        name="transaccion-list",
    ),
    path(
        "transacciones/nueva/",
        TransaccionCreateView.as_view(),
        name="transaccion-create",
    ),
    path(
        "transacciones/editar/<int:pk>/",
        TransaccionUpdateView.as_view(),
        name="transaccion-update",
    ),
    path(
        "transacciones/eliminar/<int:pk>/",
        TransaccionDeleteView.as_view(),
        name="transaccion-delete",
    ),
]