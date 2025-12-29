from pydantic import BaseModel, EmailStr

class RegistrationRequest(BaseModel):
    rut: str
    email: str
    phone: str