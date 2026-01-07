from application.service.extras.protocols import CodeNameItem
from clients.reference_clients import SynchClient
from application.data.unit_of_work import UnitOfWork
from clients.responses import DistrictCodeReponse
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("CENTRAL_URL")
TOKEN=os.getenv("TOKEN")
ENDPOINT=os.getenv("DISTRICTS_ENDPOINT")

def fetch_all_districts() -> list[CodeNameItem]:
    '''
    Special method to fetch the districts, as they require a different structure
    
    :return: Description
    :rtype: list[CodeNameItem]
    '''

    client = SynchClient(BASE_URL, TOKEN)

    # This will holds all the districts
    all_items = []

    # Get all regions in the table
    with UnitOfWork() as uow:
        region_codes = uow.references.region_references.get_existing_codes()

    # Get districts for each region
    for region_code in region_codes:
        endpoint_url = ENDPOINT + f"{region_code}"
        response = client.get_codes(
            endpoint=endpoint_url,
            response_model=DistrictCodeReponse
        )

        for d in response.districts:
            # Add the region code to each item
            d.codigo_region = region_code
            all_items.append(d)

    return all_items