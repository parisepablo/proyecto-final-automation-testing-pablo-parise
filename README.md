# Proyecto de Automatización de Pruebas API

Proyecto final para el curso Automation QA de TalentoTech, en el cual se realizan pruebas a la API de JSONPlaceholder.

## ¿Qué incluye?

- Pruebas para obtener un post específico
- Pruebas para obtener todos los posts
- Prueba para crear un nuevo post
- Generación de reporte HTML de resultados

## Tecnologías utilizadas

- Python
- pytest
- requests
- pytest-check
- pytest-html

## Requisitos

Tener Python 3 instalado y las dependencias del proyecto.

## Instalación

Ejecuta el siguiente comando en la raíz del proyecto:

```bash
pip install -r requirements.txt
```

## Ejecución de pruebas

Para ejecutar las pruebas:

```bash
pytest
```

## Estructura del proyecto

- tests/: contiene las pruebas automatizadas
- pages/: contiene la lógica para interactuar con la API
- utils/: utilidades generales como logging
- reports/: reportes generados
