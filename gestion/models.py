from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Cliente(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="cliente"
    )
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Cuenta(models.Model):
    MONEDAS = [
        ("CLP", "Peso chileno"),
        ("USD", "Dólar estadounidense"),
        ("EUR", "Euro"),
    ]

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name="cuentas"
    )
    numero = models.CharField(
        max_length=20,
        unique=True
    )
    saldo = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)]
    )
    moneda = models.CharField(
        max_length=3,
        choices=MONEDAS,
        default="CLP"
    )
    activa = models.BooleanField(default=True)
    beneficiarios = models.ManyToManyField(
        Cliente,
        blank=True,
        related_name="cuentas_como_beneficiario"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.numero} - {self.cliente.nombre}"


class Transaccion(models.Model):
    TIPOS = [
        ("DEPOSITO", "Depósito"),
        ("RETIRO", "Retiro"),
        ("TRANSFERENCIA", "Transferencia"),
    ]

    cuenta = models.ForeignKey(
        Cuenta,
        on_delete=models.PROTECT,
        related_name="transacciones"
    )
    tipo = models.CharField(
        max_length=20,
        choices=TIPOS
    )
    monto = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    descripcion = models.CharField(
        max_length=255,
        blank=True
    )
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - ${self.monto}"