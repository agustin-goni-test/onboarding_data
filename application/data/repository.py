from sqlalchemy.orm import Session
from application.data.models import CommerceRegistrationORM, ContactInfoORM
from application.domain.entities import CommerceRegistration, ContactInfo

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


class ContactInfoRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add(self, contact_info: ContactInfo) -> None:
        orm_contact_info = ContactInfoORM(
            rut=contact_info.rut,
            nombres=contact_info.nombres,
            apellidos=contact_info.apellidos,
            serial_number=contact_info.serial_number
        )
        self.db_session.add(orm_contact_info)
        self.db_session.flush()
