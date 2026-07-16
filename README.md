# EcoEncuesta

Proyecto creado por Alesandro David Fajardo Torres.

Descripción

EcoEncuesta es una aplicación de ejemplo para recolectar y analizar encuestas ambientales. Incluye:
- Backend en Python (FastAPI)
- Base de datos PostgreSQL con Docker Compose
- Redis para caché
- JupyterLab para análisis de datos
- CI con GitHub Actions

Estructura

- backend/: código del API
- notebooks/: análisis en Jupyter
- docker-compose.yml: orquesta servicios (postgres, redis, backend, jupyter)

Instrucciones rápidas

1. Instalar Docker Desktop
2. Desde la raíz del proyecto ejecutar:

   docker-compose up --build

3. Abrir http://localhost:8000 para la API y http://localhost:8888 para Jupyter

Autor: Alesandro David Fajardo Torres
