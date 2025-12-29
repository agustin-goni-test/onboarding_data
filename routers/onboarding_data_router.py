from fastapi import APIRouter
from fastapi.responses import JSONResponse
from routers.requests import RegistrationRequest
from application.service.registration_service import RegistrationService
from application.data.unit_of_work import UnitOfWork
from logger import setup_logging, get_logger
import json

setup_logging()
logger = get_logger(__name__)

# Create a router for the main app
router = APIRouter(prefix="/onboarding-data", tags=["Commerce Data"])

@router.get("/status", response_class=JSONResponse)
async def get_status():
    '''
    Endpoint to check the status of the onboarding data service
    '''
    logger.info("Status endpoint called")
    return JSONResponse(content={"status": "onboarding data service is running"})


@router.post("/registration", response_class=JSONResponse)
async def create_registration(data: RegistrationRequest):
    '''
    Endpoint to register onboarding data
    '''
    logger.info("Data registration endpoint called")
    logger.debug(f"Received data for registration: {data.model_dump()}")
    
    # Create registration service and send registration with Unit of Work
    service = RegistrationService(uow=UnitOfWork())
    service.register_commerce(
        rut=data.rut,
        email=data.email,
        phone=data.phone
    )
    
    
    logger.info("Data registered successfully")
    return JSONResponse(content={"message": "Data registered successfully"})