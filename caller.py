import requests
import argparse
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

def send_registration_data(rut: str, email: str, phone: str):
    '''
    Method to send registration data to the service
    '''

    # Sample data to register
    data = {
        "rut": rut,
        "email": email,
        "phone": phone,
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

    # Parse arguments in the call
    parser = argparse.ArgumentParser(
        description="Caller for Onboarding Data Service"
        )
    
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Option check health
    subparsers.add_parser(
        "check",
        help="Check the status of the onboarding data service"
        )
    
    # Option send registration data (with parameters)
    regsiter_parser = subparsers.add_parser(
        "register",
        help="Send registration data to the onboarding data service"
        )
    
    # Parse the parameters
    regsiter_parser.add_argument("--rut", type=str, help="RUT of the commerce", required=True)
    regsiter_parser.add_argument("--email", type=str, help="Email of the commerce", required=True)
    regsiter_parser.add_argument("--phone", type=str, help="Phone number of the commerce", required=True)

    args = parser.parse_args()

    # If health check
    if args.command == "check":
        check_service_status()
    
    # Else, if registration
    elif args.command == "register":
        send_registration_data(
            rut=args.rut,
            email=args.email,
            phone=args.phone
        )
