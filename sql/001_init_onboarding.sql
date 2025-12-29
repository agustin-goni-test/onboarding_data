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

COMMIT;
