from typing import Callable, Type, Iterable
from application.service.extras.protocols import CodeNameItem
from application.data.unit_of_work import UnitOfWork

class ReferenceSyncService:
    '''
    This class is used to handle a generic call to synchronize the services
    '''
    def __init__(
            self,
            *,
            fetch_items: Callable[[], CodeNameItem],
            uow: UnitOfWork,
            repository_attr: str,
            orm_model: Type,
            code_field: str,
            name_field: str
    ):
        self.fetch_items = fetch_items
        self.uow = uow
        self.repository_attr = repository_attr
        self.orm_model = orm_model
        self.code_field = code_field
        self.name_field = name_field

    def synch(self) -> dict:

        # 1. Get the items from the service (with client.get_codes())
        items = self.fetch_items()

        # 2. Parse the data (determine the complete list)
        incoming = {
            item.code: {
                self.code_field: item.code,
                self.name_field: item.name
            }
            for item in items
        }

        with self.uow as uow:
            # 3. Point to the attribute of the UnitOfWork to use.
            #    This is a critical point, as we will get the existing codes
            #.   (that is, select records from the table)
            repo = getattr(uow.references, self.repository_attr)
            
            # 4. Get the existing codes in the table
            existing_codes = repo.get_existing_codes()

            # 5. Determine the ones we need to insert
            to_insert = [
                self.orm_model(**data)
                for code, data in incoming.items()
                if code not in existing_codes
            ]

            # 6. If insert is needed, do it. Otherwise, do nothing
            if to_insert:
                repo.bulk_insert(to_insert)

        return {
            "received": len(incoming),
            "inserted": len(to_insert),
            "skipped": len(incoming) - len(to_insert)
        }
    
    def purge(self) -> dict:
        '''
        Purge all rows from a table
        '''

        with self.uow as uow:
            repo = getattr(uow.references, self.repository_attr)
            deleted = repo.purge()

        return {
            "purged": True,
            "deteled_rows": deleted,
            "table": self.repository_attr
        }