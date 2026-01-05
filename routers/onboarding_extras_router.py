from fastapi import APIRouter
from fastapi.responses import JSONResponse
from application.service.extras.account_type import AccountTypeSyncService
from application.service.extras.bank_code import BankCodeSyncService
from clients.account_type_client import AccountTypeClient, SynchClient
from application.data.unit_of_work import UnitOfWork
from logger import setup_logging, get_logger
from dotenv import load_dotenv
import os

# Set up logging
setup_logging()
logger = get_logger(__name__)

load_dotenv()

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
    service = AccountTypeSyncService(
        SynchClient(),
        UnitOfWork()
    )

    # Call synchronization method
    response = service.synch()
    
    # Create complete response message
    response_message={
        "message": "Account types successfully synchronized",
        "data": response
        }
    
    logger.info("OK")
    return JSONResponse(content=response_message)


@router.post("/banks", response_class=JSONResponse)
async def update_banks_list():
    '''
    Update the bank codes list table
    '''
    logger.info("Synchronizing bank codes from service...")

    # Create service with client and unit of work
    service = BankCodeSyncService(
        SynchClient(),
        UnitOfWork()
    )
    
    # Call synchronization method
    response = service.synch()
    
    # Create complete response message
    response_message={
        "message": "Account types successfully synchronized",
        "data": response
        }
    
    logger.info("OK")
    return JSONResponse(content=response_message)




