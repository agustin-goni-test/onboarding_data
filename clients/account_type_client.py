import httpx
from typing import Optional
from clients.responses import AccountTypeResponse, BankCodeResponse
from logger import setup_logging, get_logger
from dotenv import load_dotenv
import os

load_dotenv()

# Set up logging
setup_logging()
logger = get_logger(__name__)


class AccountTypeClient:
    def __init__(self, url: str, token: Optional[str] = None):
        self.base_url = url
        self.token = token

    def get_account_types(self) -> AccountTypeResponse:
        '''
        Retrieve the list of account types
        
        :param self: Description
        :return: Description
        :rtype: AccountTypeResponse
        '''
        # Add authorization header
        headers = {}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        else:
            raise Exception("No token found, cannot authenticate endopoint.")

        # Call the external service
        response = httpx.get(f"{self.base_url}", headers=headers)
        response.raise_for_status()

        logger.info("Successfully called external service to retrieve account types.")

        # Return information in appropriate response type
        return AccountTypeResponse(**response.json())



class SynchClient:
    def __init__(self):
        self.base_url = os.getenv("CENTRAL_URL")
        self.token = os.getenv("TOKEN")
        self.accounts_endpoint = os.getenv("ACCOUNTS_ENDPOINT")
        self.banks_endpoint = os.getenv("BANKS_ENDPOINT")

    def get_account_types(self) -> AccountTypeResponse:
        '''
        Retrieve the list of account types
        
        :param self: Description
        :return: Description
        :rtype: AccountTypeResponse
        '''
        # Add authorization header
        headers = {}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        else:
            raise Exception("No token found, cannot authenticate endopoint.")
        
        # Set the URL for the endpoint
        account_type_url = self.base_url + self.accounts_endpoint

        # Call the external service
        response = httpx.get(f"{account_type_url}", headers=headers)
        response.raise_for_status()

        logger.info("Successfully called external service to retrieve account types.")

        # Return information in appropriate response type
        return AccountTypeResponse(**response.json())
    

    def get_bank_codes(self):
        '''
        Docstring for get_bank_codes
        '''

        # Add authorization header
        headers = {}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        else:
            raise Exception("No authorization token provided.")
         
         # Set the URL for the endpoint
        bank_code_url = self.base_url + self.banks_endpoint

        # Call the external service
        response = httpx.get(f"{bank_code_url}", headers=headers)
        response.raise_for_status()

        logger.info("Successfully called external service to retrieve bank codes.")

        # Return information in appropriate response type
        return BankCodeResponse(**response.json())



    def get_codes(self, endpoint: str, response_model):

        # Add authorization header
        headers = {}
        if not self.token:
            raise Exception("No token provided for authorization.")
        
        headers = {"Authorization": f"Bearer {self.token}"}
        
        url = self.base_url + endpoint

        response = httpx.get(url, headers=headers)
        response.raise_for_status()

        logger.info("Successfully retrieved reference data from %s", endpoint)
        return response_model(**response.json())

