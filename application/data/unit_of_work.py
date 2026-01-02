from application.data.db import SessionLocal
from application.data.repository import CommerceRegistrationRepository, ContactInfoRepository, CommerceContactRepository, AccountInfoRepository, CommerceAccountRepository
from application.data.extras.repository import AccountReferenceRepository

class UnitOfWork:
    def __init__(self):
        self.db_session = SessionLocal()
        self.contacts = ContactInfoRepository(self.db_session)
        self.commerce_contacts = CommerceContactRepository(self.db_session)
        self.commerce_registrations = CommerceRegistrationRepository(self.db_session)
        self.accounts = AccountInfoRepository(self.db_session)
        self.commerce_accounts = CommerceAccountRepository(self.db_session)

        self.account_references = AccountReferenceRepository(self.db_session)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.db_session.rollback()
        else:
            self.db_session.commit()
        self.db_session.close()