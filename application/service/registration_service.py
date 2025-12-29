from application.domain.entities import CommerceRegistration
from application.data.unit_of_work import UnitOfWork

class RegistrationService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def register_commerce(self, rut: str, email: str, phone: str) -> None:
        registration = CommerceRegistration(
            rut=rut,
            email=email,
            phone=phone
            )
        
        with self.uow as uow:
            uow.commerce_registrations.add(registration)



    
