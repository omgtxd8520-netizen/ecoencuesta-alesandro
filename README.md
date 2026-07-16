# EcoEncuesta

Proyecto creado por Alesandro David Fajardo Torres.

Descripción

EcoEncuesta es una aplicación de ejemplo para recolectar y analizar encuestas ambientales. Incluye:
- Backend en Python (FastAPI)
- Base de datos PostgreSQL con Docker Compose
- Redis para caché
- JupyterLab para análisis de datos
- CI con GitHub Actions

Estado: v0.1.0

Estructura

- backend/: código del API
- notebooks/: análisis en Jupyter
- data/: datos de ejemplo
- docker-compose.yml: orquesta servicios (postgres, redis, backend, jupyter)

Rápido inicio (desarrollo)

1. Instalar Docker Desktop
2. Copiar variables de ejemplo:

   cp .env.example .env

3. Levantar servicios:

   docker-compose up --build

4. Inicializar esquema (una vez):

   docker-compose run --rm backend python -m backend.src.app.init_db

5. Poblar con datos de ejemplo:

   docker-compose run --rm backend python -m backend.scripts.seed_db

6. Abrir:
- API: http://localhost:8000
- JupyterLab: http://localhost:8888 (token: ecotoken)

Uso: ejemplos de API

- Crear encuesta (curl):

  curl -X POST "http://localhost:8000/surveys/" -H "Content-Type: application/json" -d '{"respondent_name":"Pedro","location":"Playa","score":4,"notes":"Limpieza regular"}'

- Obtener encuesta:

  curl http://localhost:8000/surveys/1

Tests

  docker-compose run --rm backend pytest -q

Archivos importantes

- backend/src/app: código FastAPI
- backend/scripts/seed_db.py: script para poblar la BD con data/sample_surveys.csv
- notebooks/analysis.ipynb: ejemplo de análisis con pandas

Autor: Alesandro David Fajardo Torres
