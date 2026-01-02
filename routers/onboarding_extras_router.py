from fastapi import APIRouter
from fastapi.responses import JSONResponse
from application.service.extras.account_type import AccountTypeSyncService
from clients.account_type_client import AccountTypeClient
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
async def update_banks_list():
    '''
    Update the list of banks from an external service.
    '''
    logger.info("Synchronizing account types from service...")

    url = os.getenv("CENTRAL_URL")
    token = os.getenv("TOKEN")

    account_type_client = AccountTypeClient(url=url, token=token)
    service = AccountTypeSyncService(
        account_type_client,
        UnitOfWork()
    )

    response = service.synch()

    logger.info("OK")
    return JSONResponse(content={"message": "Account types successfully synchronized"})

