# Tienda de Tecnología

## Requisitos

- Python 3.11.5
- pip 24.0

## Instalación

1. Clonar el repositorio:

```bash

python -m venv env

source env/bin/activate  # En macOS y Linux

env\Scripts\activate     # En Windows

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

```




# Orden de Pruebas y Funcionalidades

## Inicio

- **URL:** `/`
- **Descripción:** Página principal de la tienda donde se muestran las categorías disponibles.
- **Archivo:** `inicio.html`

## Agregar Producto

- **URL:** `/agregar_producto/?tipo=<tipo>`
- **Descripción:** Formulario para agregar un nuevo producto de un tipo específico (celular, computadora, televisor).
- **Archivo:** `agregar_producto.html`

## Buscar Producto

- **URL:** `/buscar_productos/`
- **Descripción:** Página para buscar productos por nombre.
- **Archivo:** `buscar_productos.html`
- **Funcionalidad de búsqueda:** El formulario de búsqueda se encuentra en el navbar (`base.html`).

## Listar Celulares

- **URL:** `/celulares/`
- **Descripción:** Página que lista todos los celulares disponibles en la tienda.
- **Archivo:** `listar_celulares.html`

## Listar Computadoras

- **URL:** `/computadoras/`
- **Descripción:** Página que lista todas las computadoras disponibles en la tienda.
- **Archivo:** `listar_computadoras.html`

## Listar Televisores

- **URL:** `/televisores/`
- **Descripción:** Página que lista todos los televisores disponibles en la tienda.
- **Archivo:** `listar_televisores.html`

## Detalle del Producto

- **URL:** `/detalle_producto/<tipo>/<id>/`
- **Descripción:** Muestra los detalles de un producto específico.
- **Archivo:** `detalle_producto.html`

## Plantillas HTML Específicas

- **Descripción:** Las plantillas HTML específicas (`agregar_producto.html`, `buscar_productos.html`, `detalle_producto.html`, `inicio.html`, `listar_celulares.html`, `listar_computadoras.html`, `listar_televisores.html`) extienden `base.html` para reutilizar la estructura común y los elementos de navegación. Esto reduce la duplicación de código y simplifica el mantenimiento.