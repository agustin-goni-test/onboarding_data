from application.domain.entities import CommerceContact
from application.data.unit_of_work import UnitOfWork

class CommerceContactService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def create_commerce_contact(
            self, 
            rut: str,
            contact_id: int
            ) -> None:
        commerce_contact = CommerceContact(
            rut=rut,
            contact_id=contact_id
        )
        
        with self.uow as uow:
            uow.commerce_contacts.add(commerce_contact)