# Makefile de conveniencia
.PHONY: up seed test initdb migrator check

up:
	docker-compose up --build

initdb:
	docker-compose run --rm migrator

seed:
	docker-compose run --rm backend python scripts/seed_db.py

migrator:
	docker-compose run --rm migrator

check:
	docker-compose run --rm backend python src/app/check_db.py

test:
	docker-compose run --rm backend pytest -q
