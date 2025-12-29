import requests
import os
from logger import setup_logging, get_logger

# Start logger
setup_logging()
logger = get_logger(__name__)


def check_service_status():
    '''
    Method to check service status
    '''

    # URL of the status endpoint
    url_status = "http://127.0.0.1:8000/onboarding-data/status"

    logger.info(f"Checking service status at {url_status}")
    try:
        response = requests.get(url_status)
        if response.status_code == 200:
            logger.info(f"Service is up and running: {response.json()}")
        else:
            logger.error(f"Service returned unexpected status code: {response.status_code}")
    except Exception as e:
        logger.error(f"Error while checking service status: {str(e)}") 

def send_registration_data():
    '''
    Method to send registration data to the service
    '''

    # Sample data to register
    data = {
        "rut": "12345678-9",
        "email": "prueba@prueba.cl",
        "phone": "+56912345678",
    }

    # URL of the registration endpoint
    url_registration = "http://127.0.0.1:8000/onboarding-data/registration"
    
    logger.info(f"Sending registration data to {url_registration}")
    
    # Send POST request to register data
    try:
        response = requests.post(url_registration, json=data)
        if response.status_code == 200:
            logger.info(f"Data registered successfully: {response.json()}")
        else:
            logger.error(f"Failed to register data, status code: {response.status_code}")
    except Exception as e:
        logger.error(f"Error while sending registration data: {str(e)}")    


if __name__ == "__main__":
    # check_service_status()
    send_registration_data()
