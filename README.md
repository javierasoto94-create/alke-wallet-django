# Alke Wallet - Django

Proyecto desarrollado para el Módulo 7: Desarrollo Web con Django, utilizando Python y Django.

## Descripción

Alke Wallet es una aplicación web de gestión financiera desarrollada con Django.

La aplicación permite administrar:

- Clientes
- Cuentas bancarias
- Transacciones
- Usuarios mediante Django Authentication
- Datos mediante Django Admin

El proyecto utiliza Django ORM para la interacción con la base de datos y Django TestCase para las pruebas automatizadas.

---

## Tecnologías utilizadas

- Python
- Django 6.1.1
- SQLite
- HTML
- Django ORM
- Django Admin
- Git
- GitHub

---

## Estructura del proyecto

```text
websolutions_platform/
│
├── gestion/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── websolutions_platform/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

## Modelos y relaciones

La aplicación utiliza tres modelos principales:

### Cliente

Representa a los clientes de la plataforma.

Campos principales:

- Usuario asociado
- Nombre
- Email
- Teléfono
- Fecha de registro

### Cuenta

Representa las cuentas bancarias asociadas a los clientes.

Campos principales:

- Cliente
- Número de cuenta
- Saldo
- Moneda
- Estado de actividad
- Beneficiarios
- Fecha de creación

### Transacción

Representa las operaciones realizadas sobre las cuentas.

Campos principales:

- Cuenta
- Tipo de transacción
- Monto
- Descripción
- Fecha

### Relaciones utilizadas

El proyecto implementa diferentes tipos de relaciones mediante Django ORM:

- `OneToOneField`: relación entre usuario y cliente.
- `ForeignKey`: relación entre cliente y cuentas.
- `ForeignKey`: relación entre cuenta y transacciones.
- `ManyToManyField`: relación entre cuentas y beneficiarios.

También se utilizan reglas `on_delete`, validadores y campos con opciones (`choices`).

---

## Base de datos

Durante el desarrollo se utiliza SQLite.

Configuración principal:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Para producción se contempla el uso de PostgreSQL mediante la configuración correspondiente en `settings.py`.

---

## Migraciones

Las migraciones de Django permiten mantener sincronizada la estructura de los modelos con la base de datos.

Comandos utilizados:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
```

La aplicación cuenta con una migración inicial:

```text
gestion/migrations/0001_initial.py
```

---

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

---

## CRUD

El proyecto implementa operaciones CRUD utilizando vistas genéricas de Django:

- `ListView`
- `CreateView`
- `UpdateView`
- `DeleteView`

Se utilizan rutas dinámicas mediante identificadores:

```text
<int:pk>
```

Los formularios utilizan Django Forms y las operaciones de creación y actualización utilizan protección CSRF.

---

## Consultas y Django ORM

Se realizaron consultas utilizando Django ORM mediante:

- `QuerySet`
- `filter()`
- `exclude()`
- `annotate()`
- `Count()`
- `values()`
- `raw()`

También se realizaron consultas mediante Django Shell.

Para consultas SQL personalizadas se utilizaron parámetros, evitando incorporar directamente valores proporcionados por el usuario en las sentencias SQL.

---

## Django Admin

El proyecto incorpora Django Admin para la administración de:

- Usuarios
- Clientes
- Cuentas
- Transacciones

Se configuraron los modelos mediante `admin.py`, incluyendo:

- `list_display`
- `search_fields`
- `list_filter`

También se creó un usuario administrador mediante:

```bash
python manage.py createsuperuser
```

El panel de administración se encuentra disponible en:

```text
http://127.0.0.1:8000/admin/
```

---

## Aplicaciones Django utilizadas

El proyecto utiliza aplicaciones preinstaladas de Django:

- `django.contrib.admin`
- `django.contrib.auth`
- `django.contrib.contenttypes`
- `django.contrib.sessions`
- `django.contrib.messages`
- `django.contrib.staticfiles`

Además, se incorpora la aplicación:

```text
gestion
```

---

## Pruebas

El proyecto cuenta con pruebas automatizadas utilizando `django.test.TestCase`.

Las pruebas verifican:

- Creación de clientes.
- Consulta de clientes en la base de datos.
- Relación entre usuario y cliente.
- Creación de cuentas.
- Relación entre cuenta y cliente.
- Creación de transacciones.
- Relación entre transacción y cuenta.

### Resultado

```text
Found 5 test(s).
.....
----------------------------------------------------------------------
Ran 5 tests in 1.287s

OK
```

Para ejecutar las pruebas:

```bash
python manage.py test
```

---

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/javierasoto94-create/alke-wallet-django.git
```

### 2. Ingresar al proyecto

```bash
cd alke-wallet-django
```

### 3. Crear un entorno virtual

Windows:

```bash
python -m venv venv
```

Activar:

```bash
venv\Scripts\activate
```

### 4. Instalar Django

```bash
pip install django
```

### 5. Ejecutar las migraciones

```bash
python manage.py migrate
```

### 6. Crear usuario administrador

```bash
python manage.py createsuperuser
```

### 7. Ejecutar el servidor

```bash
python manage.py runserver
```

Luego abrir:

```text
http://127.0.0.1:8000/
```

Panel administrativo:

```text
http://127.0.0.1:8000/admin/
```

---

## Evidencias del proyecto

Durante el desarrollo se generaron evidencias de:

- Configuración del proyecto.
- Modelos y relaciones.
- Migraciones.
- Consultas mediante Django Shell.
- Operaciones CRUD.
- Django Admin.
- Pruebas automatizadas.
- Control de versiones con Git.
- Repositorio GitHub.

---

## Control de versiones

El proyecto fue gestionado utilizando Git y GitHub.

Repositorio:

https://github.com/javierasoto94-create/alke-wallet-django

La rama principal utilizada es:

```text
main
```

---

## Autor

Javiera Soto

Proyecto académico - Módulo 7

├── manage.py
└── README.md
