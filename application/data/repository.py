from sqlalchemy.orm import Session
from application.data.models import CommerceRegistrationORM, ContactInfoORM, CommerceContactORM, AccountInfoORM, CommerceAccountORM
from application.domain.entities import CommerceRegistration, ContactInfo, CommerceContact, AccountInfo, CommerceAccount

class CommerceRegistrationRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_id_by_rut(self, rut: str) -> int:
        '''
        Return the id of the regsistration with the given RUT
        or raise ValueError if not found.
        '''
        comercio_id = (
            self.db_session.query(CommerceRegistrationORM.id)
            .filter(CommerceRegistrationORM.rut == rut)
            .scalar()
        )

        # If not found, raise an error
        if comercio_id is None:
            raise ValueError(f"Commerce with RUT '{rut}' not found.")
        
        # REturn the found id
        return comercio_id
    
    def get_registration_by_rut(self, rut: str) -> CommerceRegistration:
        orm_registration = (
            self.db_session.query(CommerceRegistrationORM)
            .filter(CommerceRegistrationORM.rut == rut)
            .one_or_none()
        )

        # If not found, raise an error
        if orm_registration is None:
            raise ValueError(f"Commerce with RUT '{rut}' not found.")
        
        # Return registration entity
        return CommerceRegistration(
            rut=orm_registration.rut,
            email=orm_registration.email,
            phone=orm_registration.phone
        )


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

    def add(self, contact_info: ContactInfo) -> int:
        orm_contact_info = ContactInfoORM(
            rut=contact_info.rut,
            nombres=contact_info.nombres,
            apellidos=contact_info.apellidos,
            serial_number=contact_info.serial_number
        )
        self.db_session.add(orm_contact_info)
        self.db_session.flush()

        return orm_contact_info.id


class CommerceContactRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add(self, contacto_com: CommerceContact) -> None:
        orm_contacto = CommerceContactORM(
            comercio_id=contacto_com.comercio_id,
            contact_id=contacto_com.contact_id,
            rol=contacto_com.rol,
            principal=contacto_com.principal
        )
        self.db_session.add(orm_contacto)


class AccountInfoRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add(self, cuenta_info: AccountInfo) -> int:
        orm_cuenta = AccountInfoORM(
            rut_titular=cuenta_info.rut_titular,
            nombre_titular=cuenta_info.nombre_titular,
            banco=cuenta_info.banco,
            tipo_cuenta=cuenta_info.tipo_cuenta
        )
        self.db_session.add(orm_cuenta)
        self.db_session.flush()

        return orm_cuenta.id


class CommerceAccountRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add(self, cuenta_com: CommerceAccount):
        orm_cuenta = CommerceAccountORM(
            comercio_id=cuenta_com.comercio_id,
            cuenta_id=cuenta_com.cuenta_id,
            principal=cuenta_com.principal
        )
        self.db_session.add(orm_cuenta)



