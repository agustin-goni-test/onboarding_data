from sqlalchemy.orm import Mapped, mapped_column
from application.data.db import Base

class CuentaORM(Base):
    __tablename__ = "cuentas"
    __table_args__ = {"schema": "onboarding_extras"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tipo_cuenta: Mapped[str] = mapped_column(nullable=False)
    codigo_tipo: Mapped[int] = mapped_column(nullable=False, unique=True)

