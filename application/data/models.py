from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from application.data.db import Base
from datetime import datetime

class CommerceRegistrationORM(Base):
    __tablename__ = "registro_comercio"
    __table_args__ = {"schema": "onboarding"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rut: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[str] = mapped_column(nullable=False)


class ContactInfoORM(Base):
    __tablename__ = "contact"
    __table_args__ = {"schema": "onboarding"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rut: Mapped[str] = mapped_column(nullable=False)
    nombres: Mapped[str] = mapped_column(nullable=False)
    apellidos: Mapped[str] = mapped_column(nullable=False)
    serial_number: Mapped[str] = mapped_column(nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=True
    )