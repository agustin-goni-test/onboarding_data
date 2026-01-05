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


class SynchClient:
    def __init__(self, url: str, token: str):
        self.base_url = url
        self.token = token

    def get_codes(self, endpoint: str, response_model):

        # Add authorization header
        headers = {}
        if not self.token:
            raise Exception("No token provided for authorization.")
        
        # Add header for authorization using token
        headers = {"Authorization": f"Bearer {self.token}"}
        
        # Set the full URL including the endpoint
        url = self.base_url + endpoint

        # Call the service and raise for status
        response = httpx.get(url, headers=headers)
        response.raise_for_status()

        logger.info("Successfully retrieved reference data from %s", endpoint)
        return response_model(**response.json())