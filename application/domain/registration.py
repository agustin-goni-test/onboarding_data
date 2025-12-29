from dataclasses import dataclass

@dataclass
class CommerceRegistration:
    rut: str
    email: str
    phone: str

    def __init__(self, rut, email, phone):
        self.rut = rut
        self.email = email
        self.phone = phone

