from clients.account_type_client import AccountTypeClient
from application.data.unit_of_work import UnitOfWork
from application.data.extras.models import CuentaORM

class AccountTypeSyncService:
    def __init__(self, client: AccountTypeClient, uow: UnitOfWork):
        self.client = client
        self.uow = uow

    def synch(self) -> dict:
        '''
        Used to synchronize information between the service and the database
        
        :param self: Description
        :return: Description
        :rtype: dict
        '''

        # 1. Call the service
        response = self.client.get_account_types()

        # 2. Parse the data
        incoming = {
            acc_type.code: {
                "codigo_tipo": acc_type.code,
                "tipo_cuenta": acc_type.name,
            }
            for acc_type in response.accountTypes
        }

        with self.uow as uow:
            # 3. Obtain DB state
            existing_codes = uow.account_references.get_existing_codes()

            # 4. Obtain diff
            to_insert = [
                CuentaORM(**data)
                for code, data in incoming.items()
                if code not in existing_codes
            ]

            # 5. Insert or do nothing
            if to_insert:
                uow.account_references.bulk_insert(to_insert)

        return {
            "received": len(incoming),
            "inserted": len(to_insert),
            "skipped": len(incoming) - len(to_insert)
        }
