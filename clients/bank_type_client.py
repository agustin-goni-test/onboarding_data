import httpx
from typing import Optional
from clients.responses import BankCodeResponse
from logger import setup_logging, get_logger

# Set up logging
setup_logging()
logger = get_logger(__name__)


class BankCodeClient:
    def __init__(self, url: str, token: Optional[str] = None):
        self.base_url = url
        self.token = token

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
         
        # Call the external service
        response = httpx.get(f"{self.base_url}", headers=headers)
        response.raise_for_status()

        logger.info("Successfully called external service to retrieve bank codes.")

        # Return information in appropriate response type
        return BankCodeResponse(**response.json())
