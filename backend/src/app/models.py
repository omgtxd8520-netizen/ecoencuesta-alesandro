# Esquema de tablas (SQL simple). En producción usar Alembic para migraciones.

CREATE TABLE IF NOT EXISTS surveys (
    id SERIAL PRIMARY KEY,
    respondent_name TEXT,
    location TEXT,
    score INTEGER,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
