from fastapi import APIRouter
from fastapi.responses import JSONResponse
from application.service.extras.services import ReferenceSyncService
from clients.reference_clients import SynchClient
from clients.responses import AccountTypeResponse, BankCodeResponse, RegionCodeResponse
from application.data.extras.models import CuentaORM, BancoORM, RegionORM, ComunaORM
from application.data.unit_of_work import UnitOfWork
from logger import setup_logging, get_logger
from dotenv import load_dotenv
from application.service.extras.fetch_reference_data import fetch_all_districts
import os

# Set up logging
setup_logging()
logger = get_logger(__name__)

load_dotenv()

BASE_URL = os.getenv("CENTRAL_URL")
TOKEN=os.getenv("TOKEN")

# Create a router to add to the main app
router = APIRouter(prefix="/onboarding-extras", tags=["Commerce Extras"])

@router.get("/status", response_class=JSONResponse)
async def get_status():
    '''
    Endpoint to check the status of the onboarding extras data service
    '''
    logger.info("Status endpoint called")
    return JSONResponse(content={"status": "onboarding extras data service is running"})


@router.post("/accounts", response_class=JSONResponse)
async def update_accounts_list():
    '''
    Update the list of banks from an external service.
    '''
    logger.info("Synchronizing account types from service...")

    # Create service with client and unit of work
    service = ReferenceSyncService(
        fetch_items=lambda: SynchClient(BASE_URL, TOKEN)
            .get_codes(os.getenv("ACCOUNTS_ENDPOINT"), AccountTypeResponse)
            .account_types,
        uow=UnitOfWork(),
        repository_attr="account_references",
        orm_model=CuentaORM,
        code_field="codigo_tipo",
        name_field="tipo_cuenta"
    )

    return {
        "message": "Account types synchronized successfully",
        "data": service.synch()
    }    


@router.post("/banks", response_class=JSONResponse)
async def update_banks_list():
    '''
    Update the bank codes list table
    '''
    logger.info("Synchronizing bank codes from service...")

    # Create service with client and unit of work
    service = ReferenceSyncService(
        fetch_items=lambda:SynchClient(BASE_URL, TOKEN)
            .get_codes(os.getenv("BANKS_ENDPOINT"), BankCodeResponse)
            .bank_codes,
        uow=UnitOfWork(),
        repository_attr="bank_references",
        orm_model=BancoORM,
        code_field="codigo_banco",
        name_field="nombre_banco"
    )

    return {
        "message": "Account types synchronized successfully",
        "data": service.synch()
    }

@router.post("/regions", response_class=JSONResponse)
async def update_regions_list():
    '''
    Update the regions list
    '''

    logger.info("Synchronizing region codes from service...")

    # Create the service with client and unit of work
    service = ReferenceSyncService(
        fetch_items=lambda:SynchClient(BASE_URL, TOKEN)
            .get_codes(os.getenv("REGIONS_ENDPOINT"), RegionCodeResponse)
            .regions,
        uow=UnitOfWork(),
        repository_attr="region_references",
        orm_model=RegionORM,
        code_field="codigo_region",
        name_field="nombre_region"
    )

    return {
        "message": "Region codes synchronized successfully",
        "data": service.synch()
    }


@router.post("/districts", response_class=JSONResponse)
async def update_district_list():
    '''
    Update the districts list
    '''

    logger.info("Synchronizing district codes from service...")
    
    service = ReferenceSyncService(
        fetch_items=fetch_all_districts,
        uow=UnitOfWork(),
        repository_attr="district_references",
        orm_model=ComunaORM,
        code_field="codigo_comuna",
        name_field="nombre_comuna",
        extra_fields=["codigo_region"]
    )

    return {
        "message": "District codes synchronized successfully",
        "data": service.synch()
    }



@router.post("/accounts/purge", response_class=JSONResponse)
async def purge_account_types():
    '''
    Delete all account types from the database
    '''
    service = ReferenceSyncService(
        fetch_items=[],  # Not used here
        uow=UnitOfWork(),
        repository_attr="account_references",
        orm_model=CuentaORM,
        code_field="codigo_tipo",
        name_field="tipo_cuenta"
    )

    return {
        "message": "Account types purged successfully",
        "data": service.purge()
    }

@router.post("/banks/purge", response_class=JSONResponse)
async def purge_bank_codes():
    '''
    Delete all bank codes from database
    '''
    service = ReferenceSyncService(
        fetch_items=[],  # Not used here
        uow=UnitOfWork(),
        repository_attr="bank_references",
        orm_model=BancoORM,
        code_field="codigo_banco",
        name_field="nombre_banco"
    )

    return {
        "message": "Bank codes purged successfully",
        "data": service.purge()
    }




