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

@dataclass
class ContactInfo:
    rut: str
    nombres: str
    apellidos: str
    serial_number: str

    def __init__(self, rut, nombres, apellidos, serial_number):
        self.rut = rut
        self.nombres = nombres
        self.apellidos = apellidos
        self.serial_number = serial_number