from django.test import TestCase
from django.contrib.auth.models import User

from .models import Cliente, Cuenta, Transaccion


class ClienteModelTest(TestCase):

    def setUp(self):
        self.usuario = User.objects.create_user(
            username="usuario_prueba",
            password="12345678"
        )

        self.cliente = Cliente.objects.create(
            usuario=self.usuario,
            nombre="Cliente Test",
            email="cliente@test.com",
            telefono="987654321"
        )

    def test_cliente_creado_correctamente(self):
        self.assertEqual(self.cliente.nombre, "Cliente Test")
        self.assertEqual(self.cliente.email, "cliente@test.com")

    def test_cliente_se_encuentra_en_base_de_datos(self):
        cliente = Cliente.objects.get(email="cliente@test.com")
        self.assertEqual(cliente.nombre, "Cliente Test")

    def test_relacion_usuario_cliente(self):
        self.assertEqual(self.cliente.usuario.username, "usuario_prueba")


class CuentaModelTest(TestCase):

    def setUp(self):
        self.usuario = User.objects.create_user(
            username="cuenta_test",
            password="12345678"
        )

        self.cliente = Cliente.objects.create(
            usuario=self.usuario,
            nombre="Cliente Cuenta",
            email="cuenta@test.com",
            telefono="912345678"
        )

    def test_cliente_puede_tener_cuenta(self):
        cuenta = Cuenta.objects.create(
            cliente=self.cliente,
            numero="CLP-TEST-0001",
            saldo=100000,
            moneda="CLP",
            activa=True
        )

        self.assertEqual(cuenta.cliente, self.cliente)
        self.assertEqual(cuenta.saldo, 100000)
        self.assertEqual(cuenta.moneda, "CLP")
        self.assertTrue(cuenta.activa)


class TransaccionModelTest(TestCase):

    def setUp(self):
        self.usuario = User.objects.create_user(
            username="transaccion_test",
            password="12345678"
        )

        self.cliente = Cliente.objects.create(
            usuario=self.usuario,
            nombre="Cliente Transaccion",
            email="transaccion@test.com",
            telefono="912345678"
        )

        self.cuenta = Cuenta.objects.create(
            cliente=self.cliente,
            numero="CLP-TEST-0002",
            saldo=100000,
            moneda="CLP",
            activa=True
        )

    def test_transaccion_creada_correctamente(self):
        transaccion = Transaccion.objects.create(
            cuenta=self.cuenta,
            tipo="DEPOSITO",
            monto=50000,
            descripcion="Depósito de prueba"
        )

        self.assertEqual(transaccion.cuenta, self.cuenta)
        self.assertEqual(transaccion.tipo, "DEPOSITO")
        self.assertEqual(transaccion.monto, 50000)
        self.assertEqual(
            transaccion.descripcion,
            "Depósito de prueba"
        )