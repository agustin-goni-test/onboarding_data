import httpx
from typing import Optional
from clients.responses import AccountTypeResponse
from logger import setup_logging, get_logger

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

        # Call the external service
        response = httpx.get(f"{self.base_url}", headers=headers)
        response.raise_for_status()

        logger.info("Successfully called external service to retrieve account types.")

        # Return information in appropriate response type
        return AccountTypeResponse(**response.json())
