from pydantic import BaseModel, EmailStr

class RegistrationRequest(BaseModel):
    rut: str
    email: str
    phone: str


class ContactRequest(BaseModel):
    rut: str
    nombres: str
    apellidos: str
    serial_number: str


class RepresentativeRequest(BaseModel):
    rut_comercio: str
    rut: str
    nombres: str
    apellidos: str
    serial_number: str
    principal: bool