from sqlalchemy.orm import Session
from sqlalchemy import Column
from typing import Generic, TypeVar
from application.data.extras.models import CuentaORM, BancoORM
from application.domain.extra_entities import AccountReference

T = TypeVar("T")

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


class BankReferenceRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_existing_codes(self) -> set[int]:
        '''
        Obtain all codes for the list of banks in the database
        
        :param self: Description
        :return: Description
        :rtype: set[int]
        '''

        return {
            row[0]
            for row in (
                self.db_session.query(BancoORM.codigo_banco).all()
            )
        }
    
    def bulk_insert(self, bancos: list[BancoORM]) -> None:
        self.db_session.add_all(bancos)


class ReferenceRepository:
    '''
    Generic repository class for all reference tables of the same structure
    '''
    def __init__(
            self,
            db_session: Session,
            model: type[T],
            code_column: Column,
    ):
        self.db_session = db_session
        self.model = model
        self.code_column = code_column

    def get_existing_codes(self) -> set[int]:
        '''
        Get existing codes already stored in the database
        
        :param self: Self
        :return: Returns a list of rows in the ORM model passed during invocation.
        :rtype: set[int]
        '''
        return {
            row[0]
            for row in (
                self.db_session.query(self.code_column).all()
            )
        }
    
    def bulk_insert(self, items: list[T]) -> None:
        '''
        Inserts a collection of rows into the database
        
        :param self: Self
        :param items: List of items to be inserted
        :type items: list[T]
        '''
        self.db_session.add_all(items)

    def purge(self) -> int:
        '''
        Eliminate all records
        
        :param self: Description
        '''
        return self.db_session.query(self.model).delete()

    



