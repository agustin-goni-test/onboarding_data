BEGIN;

-- 1. Create schema
CREATE SCHEMA IF NOT EXISTS onboarding_extras

-- 2. Create tables
CREATE TABLE IF NOT EXISTS onboarding_extras.bancos (
    id              SERIAL PRIMARY KEY,
    nombre_banco    TEXT NOT NULL,
    codigo_banco    INT NOT NULL

    CONSTRAINT bancos_codigo_banco_uk UNIQUE (codigo_banco)

);

CREATE TABLE IF NOT EXISTS onboarding_extras.cuentas (
    id              SERIAL PRIMARY KEY,
    tipo_cuenta     TEXT NOT NULL,
    codigo_tipo     INT NOT NULL

    CONSTRAINT cuentas_codigo_tipo_uk UNIQUE (codigo_tipo)
);

CREATE TABLE IF NOT EXISTS onboarding_extras.regiones (
    id              SERIAL PRIMARY KEY,
    nombre_region   TEXT NOT NULL,
    codigo_region   INT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS onboarding_extras.comunas (
    id              SERIAL PRIMARY KEY,
    codigo_region   INT NOT NULL REFERENCES onboarding_extras.regiones(codigo_region),
    codigo_comuna   INT NOT NULL,
    nombre_comuna   TEXT NOT NULL,

    UNIQUE(codigo_region, codigo_comuna);
);

COMMIT;