from application.domain.entities import ContactInfo, CommerceContact
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


class CommerceContactService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
        

    def create_commerce_contact(
            self, 
            commerce_id: int,
            contact_id: int,
            rol: str,
            principal: bool
            ) -> None:
        commerce_contact = CommerceContact(
            commerce_id=commerce_id,
            contact_id=contact_id,
            rol=rol,
            principal=principal
        )
        
        with self.uow as uow:
            uow.commerce_contacts.add(commerce_contact)


    def create_contact_as_representative(
            self,
            rut_comercio: str,
            rut: str,
            nombres: str,
            apellidos: str,
            serial_number: str,
            principal: bool = True
            ) -> None:
        with self.uow as uow:

            # 1. Create contact info
            contact_info = ContactInfo(
                rut=rut,
                nombres=nombres,
                apellidos=apellidos,
                serial_number=serial_number
            )
            contact_id = uow.contacts.add(contact_info)

            # 2. Get comercio_id by rut_comercio
            comercio_id = uow.commerce_registrations.get_id_by_rut(rut_comercio)

            # 3. Create commerce contact link
            commerce_contact = CommerceContact(
                comercio_id=comercio_id,
                contact_id=contact_id,
                rol="Representante Legal",
                principal=principal
            )
            uow.commerce_contacts.add(commerce_contact)
            