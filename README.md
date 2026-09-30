# Alke Wallet - Django

Proyecto desarrollado para el Módulo 7, utilizando Django y Python.

## Descripción

Alke Wallet es una aplicación web de gestión financiera desarrollada con Django.

Permite administrar:

- Clientes
- Cuentas bancarias
- Transacciones
- Usuarios mediante Django Authentication
- Administración de datos mediante Django Admin

## Tecnologías utilizadas

- Python
- Django 6.1.1
- SQLite
- HTML
- Django ORM
- Django Admin
- Git y GitHub

## Funcionalidades

### Clientes
- Crear clientes
- Listar clientes
- Editar clientes
- Eliminar clientes

### Cuentas
- Crear cuentas
- Listar cuentas
- Editar cuentas
- Eliminar cuentas
- Manejo de monedas
- Estado de cuenta activa/inactiva
- Relación con clientes
- Relación de beneficiarios

### Transacciones
- Registrar depósitos
- Registrar retiros
- Registrar transferencias
- Editar transacciones
- Eliminar transacciones
- Relación con cuentas

## Base de datos

El proyecto utiliza SQLite durante el desarrollo y Django ORM para el acceso a los datos.

Los principales modelos son:

- Cliente
- Cuenta
- Transaccion

Las relaciones utilizadas incluyen:

- OneToOneField
- ForeignKey
- ManyToManyField

## Administración

El proyecto incorpora Django Admin para gestionar:

- Usuarios
- Clientes
- Cuentas
- Transacciones

## Consultas y ORM

Se utilizaron consultas mediante Django ORM, incluyendo:

- QuerySets
- filter()
- annotate()
- Count()
- raw()
- consultas SQL parametrizadas

También se realizaron pruebas mediante Django Shell.

## Pruebas

El proyecto cuenta con pruebas automatizadas utilizando Django TestCase.

Resultado de las pruebas:

**5 tests ejecutados correctamente.**

## Autor

Javiera Soto

Proyecto académico - Módulo 7
