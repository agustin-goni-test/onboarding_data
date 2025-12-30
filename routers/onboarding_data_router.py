from fastapi import APIRouter
from fastapi.responses import JSONResponse
from routers.requests import RegistrationRequest, ContactRequest, RepresentativeRequest
from application.service.registration_service import RegistrationService
from application.service.contact_service import ContactService, CommerceContactService
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


@router.post("/contact", response_class=JSONResponse)
async def create_contact(data: ContactRequest):
    '''
    Endpoint to submit contact information
    
    :param data: Description
    :type data: ContactRequest
    '''
    logger.info("Contact endpoint called.")
    logger.debug(f"Received contact data: {data.model_dump()}")

    # Add logic to handle contact data here
    service = ContactService(uow=UnitOfWork())
    service.create_contact(
        rut=data.rut,
        nombres=data.nombres,
        apellidos=data.apellidos,
        serial_number=data.serial_number
    )

    logger.info("Contact data processed successfully.")
    return JSONResponse(content={"message": "Contact data processed successfully"})



@router.post("/representative", response_class=JSONResponse)
async def create_representative(data: RepresentativeRequest):
    '''
    Endpoint to submit representative contact information
    
    :param data: Description
    :type data: ContactRequest
    '''
    logger.info("Representative contact endpoint called.")
    logger.debug(f"Received representative contact data: {data.model_dump()}")

    # Add logic to handle representative contact data here
    service = CommerceContactService(uow=UnitOfWork())
    service.create_contact_as_representative(
        rut_comercio=data.rut_comercio,
        rut=data.rut,
        nombres=data.nombres,
        apellidos=data.apellidos,
        serial_number=data.serial_number,
        principal=True
    )

    logger.info("Representative contact data processed successfully.")
    return JSONResponse(content={"message": "Successfully processed representative contact data"})
