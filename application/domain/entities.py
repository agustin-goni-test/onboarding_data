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


@dataclass
class CommerceContact:
    comercio_id: int
    contact_id: int
    rol: str
    principal: bool

    def __init__(self, comercio_id, contact_id, rol, principal):
        self.comercio_id = comercio_id
        self.contact_id = contact_id
        self.rol = rol
        self.principal = principal


@dataclass
class AccountInfo:
    rut_titular: str
    nombre_titular: str
    banco: int
    tipo_cuenta: int

    def __init__(self, rut_titular, nombre_titular, banco, tipo_cuenta):
        self.rut_titular = rut_titular
        self.nombre_titular = nombre_titular
        self.banco = banco
        self.tipo_cuenta = tipo_cuenta


@dataclass
class CommerceAccount:
    comercio_id: int
    cuenta_id: int
    principal: bool

    def __init__(self, comercio_id, cuenta_id, principal):
        self.comercio_id = comercio_id
        self.cuenta_id = cuenta_id
        self.principal = principal