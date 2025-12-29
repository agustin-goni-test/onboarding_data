from sqlalchemy.orm import Session
from application.data.models import CommerceRegistrationORM
from application.domain.registration import CommerceRegistration

class CommerceRegistrationRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add(self, registration: CommerceRegistration) -> None:
        orm_registration = CommerceRegistrationORM(
            rut=registration.rut,
            email=registration.email,
            phone=registration.phone
        )
        self.db_session.add(orm_registration)
        # self.db_session.commit()
        # self.db_session.refresh(orm_registration)
        # return CommerceRegistration(
        #     rut=orm_registration.rut,
        #     email=orm_registration.email,
        #     phone=orm_registration.phone
        # )