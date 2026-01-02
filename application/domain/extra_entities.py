from dataclasses import dataclass

@dataclass
class AccountReference:
    tipo_cuenta: str
    codigo_cuenta: int

    def __init__(self, tipo_cuenta, codigo_cuenta):
        self.tipo_cuenta = tipo_cuenta
        self.codigo_cuenta = codigo_cuenta