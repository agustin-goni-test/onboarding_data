from sqlalchemy.orm import Mapped, mapped_column
from application.data.db import Base

class CommerceRegistrationORM(Base):
    __tablename__ = "registro_comercio"
    __table_args__ = {"schema": "onboarding"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rut: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[str] = mapped_column(nullable=False)