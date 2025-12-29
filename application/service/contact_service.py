from application.domain.entities import ContactInfo
from application.data.unit_of_work import UnitOfWork

class ContactService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def create_contact(
            self, 
            rut: str,
            nombres: str,
            apellidos: str,
            serial_number
            ) -> None:
        contact_info = ContactInfo(
            rut=rut,
            nombres=nombres,
            apellidos=apellidos,
            serial_number=serial_number
        )
        
        with self.uow as uow:
            uow.contacts.add(contact_info)