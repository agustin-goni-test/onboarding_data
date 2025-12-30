from dataclasses import dataclass

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