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


def check_service_status_extras():
    '''
    Method to check service status
    '''

    # URL of the status endpoint
    url_status = "http://127.0.0.1:8000/onboarding-extras/status"

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

    # Data to send
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


def send_contact_data(
        rut: str,
        nombres: str,
        apellidos: str,
        serial_number: str
):
    '''
    Method to send contact data to the service
    '''
    # Data to send
    data = {
        "rut": rut,
        "nombres": nombres,
        "apellidos": apellidos,
        "serial_number": serial_number
    }

    url_contact = "http://127.0.0.1:8000/onboarding-data/contact"

    logger.info(f"Sending contact data to {url_contact}")

    try:
        response = requests.post(url_contact, json=data)
        if response.status_code == 200:
            logger.info(f"Contact data sent successfully: {response.json()}")
        else:
            logger.error(f"Failed to send contact data, status code: {response.status_code}")
    except Exception as e:
        logger.error(f"Error while sending contact data: {str(e)}")


def send_representative_data(
        rut_comercio: str,
        rut: str,
        nombres: str,
        apellidos: str,
        serial_number: str
):
    '''
    Method to send representative contact data to the service
    '''
    # Data to send
    data = {
        "rut_comercio": rut_comercio,
        "rut": rut,
        "nombres": nombres,
        "apellidos": apellidos,
        "serial_number": serial_number,
        "principal": True
    }

    url_representative_contact = "http://127.0.0.1:8000/onboarding-data/representative"

    logger.info(f"Sending representative contact data to {url_representative_contact}")

    try:
        response = requests.post(url_representative_contact, json=data)
        if response.status_code == 200:
            logger.info(f"Representative contact data sent successfully: {response.json()}")
        else:
            logger.error(f"Failed to send representative contact data, status code: {response.status_code}")
    except Exception as e:
        logger.error(f"Error while sending representative contact data: {str(e)}")


def send_account_data (
        rut_titular: str,
        nombre_titular: str,
        banco: int,
        tipo_cuenta: int
):
    '''
    Method to send account data to the service
    
    :param rut_titular: Description
    :type rut_titular: str
    :param nombre_titular: Description
    :type nombre_titular: str
    :param banco: Description
    :type banco: int
    :param tipo_cuenta: Description
    :type tipo_cuenta: int
    '''
    data = {
        "rut_titular": rut_titular,
        "nombre_titular": nombre_titular,
        "banco": banco,
        "tipo_cuenta": tipo_cuenta
    }

    url_account = "http://127.0.0.1:8000/onboarding-data/account"

    logger.info(f"Sending account data to {url_account}")

    try:
        response = requests.post(url_account, json=data)
        if response.status_code == 200:
            logger.info(f"Account data sent successfully: {response.json()}")
        else:
            logger.error(f"Failed to send account data, status code: {response.status_code}")
    except Exception as e:
        logger.error(f"Error while sending account data: {str(e)}")


def send_account_for_commerce_data(
        rut_comercio: str,
        rut_titular: str,
        nombre_titular: str,
        banco: int,
        tipo_cuenta: int
):
    '''
    Docstring for send_account_for_commerce_data
    
    :param rut_comercio: Description
    :type rut_comercio: str
    :param rut_titular: Description
    :type rut_titular: str
    :param nombre_titular: Description
    :type nombre_titular: str
    :param banco: Description
    :type banco: int
    :param tipo_cuenta: Description
    :type tipo_cuenta: int
    '''
    data = {
        "rut_comercio": rut_comercio,
        "rut_titular": rut_titular,
        "nombre_titular": nombre_titular,
        "banco": banco,
        "tipo_cuenta": tipo_cuenta
    }

    url_commerce_account = "http://127.0.0.1:8000/onboarding-data/commerce-account"

    logger.info(f"Sending account data to {url_commerce_account}")

    try:
        response = requests.post(url_commerce_account, json=data)
        if response.status_code == 200:
            logger.info(f"Account data sent successfully: {response.json()}")
        else:
            logger.error(f"Failed to send account data, status code: {response.status_code}")
    except Exception as e:
        logger.error(f"Error while sending account data: {str(e)}")


def send_account_type_synch():
    
    url_synch = "http://127.0.0.1:8000/onboarding-extras/accounts"

    logger.info(f"Sending account data to {url_synch}")

    try:
        response = requests.post(url_synch)
        if response.status_code == 200:
            logger.info(f"Account types synchronized successfully: {response.json()}")
        else:
            logger.error(f"Failed to synchronize account types, status code: {response.status_code}")
    except Exception as e:
        logger.error(f"Error while synchronizing account types: {str(e)}")


def send_bank_type_synch():
    
    url_synch = "http://127.0.0.1:8000/onboarding-extras/banks"

    logger.info(f"Sending account data to {url_synch}")

    try:
        response = requests.post(url_synch)
        if response.status_code == 200:
            logger.info(f"Account types synchronized successfully: {response.json()}")
        else:
            logger.error(f"Failed to synchronize account types, status code: {response.status_code}")
    except Exception as e:
        logger.error(f"Error while synchronizing account types: {str(e)}")


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
    register_parser = subparsers.add_parser(
        "register",
        help="Send registration data to the onboarding data service"
        )
    
    contact_parser = subparsers.add_parser(
        "contact",
        help="Send contact data to the onboarding data service"
        )
    
    representative_parser = subparsers.add_parser(
        "representative",
        help="Send representative contact data to the onboarding data service"
        )
    
    account_parser = subparsers.add_parser(
        "account",
        help="Send account data to the onboarding data service"
    )

    commerce_account_parser = subparsers.add_parser(
        "commerce-account",
        help="Send account data to be linked to a specific commerce"
    )

    account_synch_parser = subparsers.add_parser(
        "account-synch",
        help="Synchronize the account type data"
    )

    bank_synch_parser = subparsers.add_parser(
        "bank-synch",
        help="Synchronize the bank code type data"
    )
    
    # Parse the parameters for registration
    register_parser.add_argument("--rut", type=str, help="RUT of the commerce", required=True)
    register_parser.add_argument("--email", type=str, help="Email of the commerce", required=True)
    register_parser.add_argument("--phone", type=str, help="Phone number of the commerce", required=True)

    # Parse the parameters for contact
    contact_parser.add_argument("--rut", type=str, help="RUT of the contact", required=True)
    contact_parser.add_argument("--nombres", type=str, help="First names of the contact", required=True)
    contact_parser.add_argument("--apellidos", type=str, help="Last names of the contact", required=True)
    contact_parser.add_argument("--serial_number", type=str, help="Serial number of the contact", required=True)

    # Parse the parameters for representative contact
    representative_parser.add_argument("--rut_comercio", type=str, help="RUT of the commerce", required=True)
    representative_parser.add_argument("--rut", type=str, help="RUT of the representative contact", required=True)
    representative_parser.add_argument("--nombres", type=str, help="First names of the representative contact", required=True)
    representative_parser.add_argument("--apellidos", type=str, help="Last names of the representative contact", required=True)
    representative_parser.add_argument("--serial_number", type=str, help="Serial number of the representative contact", required=True)

    account_parser.add_argument("--rut_titular", type=str, help="RUT of the account owner", required=True)
    account_parser.add_argument("--nombre_titular", type=str, help="Name of the account owner", required=True)
    account_parser.add_argument("--banco", type=int, help="Bank code of issuer bank", required=True)
    account_parser.add_argument("--tipo_cuenta", type=int, help="Account type code", required=True)

    commerce_account_parser.add_argument("--rut_comercio", type=str, help="RUT of the commerce", required= True)
    commerce_account_parser.add_argument("--rut_titular", type=str, help="RUT of the account owner", required=True)
    commerce_account_parser.add_argument("--nombre_titular", type=str, help="Name of the account owner", required=True)
    commerce_account_parser.add_argument("--banco", type=int, help="Bank code of issuer bank", required=True)
    commerce_account_parser.add_argument("--tipo_cuenta", type=int, help="Account type code", required=True)

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

    # Else, if contact
    elif args.command == "contact":
        send_contact_data(
            rut=args.rut,
            nombres=args.nombres,
            apellidos=args.apellidos,
            serial_number=args.serial_number
        )

    # Else, if representative contact
    elif args.command == "representative":
        send_representative_data(
            rut_comercio=args.rut_comercio,
            rut=args.rut,
            nombres=args.nombres,
            apellidos=args.apellidos,
            serial_number=args.serial_number
        )

    # Else, if account
    elif args.command == "account":
        send_account_data(
            rut_titular=args.rut_titular,
            nombre_titular=args.nombre_titular,
            banco=args.banco,
            tipo_cuenta=args.tipo_cuenta
        )

    # Else, if account for commmerce
    elif args.command == "commerce-account":
        send_account_for_commerce_data(
            rut_comercio=args.rut_comercio,
            rut_titular=args.rut_titular,
            nombre_titular=args.nombre_titular,
            banco=args.banco,
            tipo_cuenta=args.tipo_cuenta
        )

    # Else, if account type synchronization
    elif args.command == "account-synch":
        send_account_type_synch()
        # check_service_status_extras()

    elif args.command == "bank-synch":
        send_bank_type_synch()
