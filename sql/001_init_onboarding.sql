-- ===============================
-- Database bootstrap (PostgreSQL)
-- ===============================

BEGIN;

-- 1. Create schema
CREATE SCHEMA IF NOT EXISTS onboarding;

-- 2. Create table
CREATE TABLE IF NOT EXISTS onboarding.registro_comercio (
    id      BIGSERIAL PRIMARY KEY,
    rut     TEXT NOT NULL UNIQUE,
    email   TEXT NOT NULL,
    phone   TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS onboarding.contact (
    id      BIGSERIAL PRIMARY KEY,
    rut     TEXT NOT NULL,
    nombres TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    serial_number TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS onboarding.comercio_contacto (
    comercio_id     BIGINT NOT NULL,
    contact_id      BIGINT NOT NULL,
    rol             TEXT NOT NULL,
    principal       BOOLEAN DEFAULT FALSE,
    created_at      TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (comercio_id, contact_id, rol),

    CONSTRAINT fk_comercio
        FOREIGN KEY(comercio_id)
            REFERENCES onboarding.registro_comercio(id)
            ON DELETE CASCADE,

    CONSTRAINT fk_contact
        FOREIGN KEY(contact_id)
            REFERENCES onboarding.contact(id)
            ON DELETE CASCADE
);

COMMIT;
