# Makefile de conveniencia
.PHONY: up seed test initdb

up:
	docker-compose up --build

initdb:
	docker-compose run --rm backend python -m backend.src.app.init_db

seed:
	docker-compose run --rm backend python -m backend.scripts.seed_db

test:
	docker-compose run --rm backend pytest -q
