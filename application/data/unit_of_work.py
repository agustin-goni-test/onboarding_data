from application.data.db import SessionLocal
from application.data.repository import CommerceRegistrationRepository

class UnitOfWork:
    def __init__(self):
        self.db_session = SessionLocal()
        self.commerce_registrations = CommerceRegistrationRepository(self.db_session)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.db_session.rollback()
        else:
            self.db_session.commit()
        self.db_session.close()