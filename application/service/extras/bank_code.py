from clients.bank_type_client import BankCodeClient
from clients.account_type_client import SynchClient
from application.data.unit_of_work import UnitOfWork
from application.data.extras.models import BancoORM

class BankCodeSyncService:
    def __init__(self, client: SynchClient, uow: UnitOfWork):
        self.client = client
        self.uow = uow

    def synch(self, endpoint: str) -> dict:
        '''
        Used to synchronize information between the service and the database.
        Handles bank codes.
        
        :param self: Description
        :return: Description
        :rtype: dict
        '''

        # 1. Call the service
        response = self.client.get_bank_codes()

        # 2. Parse the data
        incoming = {
            bank_code.code: {
                "nombre_banco": bank_code.name,
                "codigo_banco": bank_code.code
            }
            for bank_code in response.bank_codes
        }

        with self.uow as uow:
            # 3. Obtain DB state
            existing_codes = uow.bank_references.get_existing_codes()

            # 4. Obtain diff
            to_insert = [
                BancoORM(**data)
                for code, data in incoming.items()
                if code not in existing_codes
            ]

            # 5. Bulk insert or do nothing
            if to_insert:
                uow.bank_references.bulk_insert(to_insert)
        
        return {
            "received": len(incoming),
            "inserted": len(to_insert),
            "skipped": len(incoming) - len(to_insert)
        }
