from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from logger import setup_logging, get_logger
from routers import onboarding_data_router
from infrastructure.db_validation.registration_contract import validate_registration_insert_contract
from infrastructure.db_validation.contact_contract import validate_contact_insert_contract
from infrastructure.db_validation.generic_contract import validate_generic_contract
from application.data.models import CommerceRegistrationORM, ContactInfoORM, CommerceContactORM
from application.data.models import AccountInfoORM, CommerceAccountORM
from application.data.db import engine
import sys

# -------------------------------------------------------------------
# Logging setup
# -------------------------------------------------------------------
setup_logging()
logger = get_logger(__name__)

# -------------------------------------------------------------------
# OpenAPI tags metadata
# -------------------------------------------------------------------
tags_metadata = [
    {
        "name": "status",
        "description": "Checks the status of the service"
    }
]

# -------------------------------------------------------------------
# Application lifecycle events
# -------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    logger.info("Application startup: Onboarding Data Service")

    # Validate database schema and tables
    run_startup_validations()

    logger.info("Database validation completed successfully.")

    yield
    
    # Shutdown actions
    logger.info("Application shutdown: Onboarding Data Service")


# -------------------------------------------------------------------
# Create FASTAPI app
# -------------------------------------------------------------------
app = FastAPI(
    title="Onboarding Data Service",
    description="API for managing onboarding data",
    version="0.0.1",
    openapi_tags=tags_metadata,
    lifespan=lifespan
    )

# -------------------------------------------------------------------
# Create router(s) and include in app
# -------------------------------------------------------------------
app.include_router(onboarding_data_router.router)

# -------------------------------------------------------------------
# Create middleware for logging
# -------------------------------------------------------------------
@app.middleware("http")
async def log_requests(request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")
    try:
        response = await call_next(request)
        logger.info(f"Response status: {response.status_code} for {request.method} {request.url}")
        return response
    
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise

# -------------------------------------------------------------------
# Validations to be run at startup time
# -------------------------------------------------------------------
def run_startup_validations():
    '''
    Method to run startup validations
    '''
    logger.info("Running startup validations...")
    try:
        validate_registration_insert_contract(
            engine=engine,
            orm_model=CommerceRegistrationORM
        )

        validate_contact_insert_contract(
            engine=engine,
            orm_model=ContactInfoORM
        )

        validate_generic_contract(
            engine=engine,
            orm_model=CommerceContactORM
        )

        validate_generic_contract (
            engine=engine,
            orm_model=AccountInfoORM
        )

        validate_generic_contract (
            engine=engine,
            orm_model=CommerceAccountORM
        )

    except Exception as e:
        logger.critical(f"Startup validation failed: {str(e)}")
        
        # Validation didn't work, API cannot continue
        sys.exit(1)
        

    logger.info("Startup validations completed successfully.")