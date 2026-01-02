from sqlalchemy.orm import Session
from application.data.extras.models import CuentaORM
from application.domain.extra_entities import AccountReference

class AccountReferenceRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_existing_codes(self) -> set[int]:
        '''
        Obtain all account codes currently stored in the database
        
        :param self: Description
        :return: Description
        :rtype: set[int]
        '''
        return {
            row[0]
            for row in (
                self.db_session.query(CuentaORM.codigo_tipo).all()
            )
        }
    
    def bulk_insert(self, cuentas: list[CuentaORM]) -> None:
        self.db_session.add_all(cuentas)



