from sqlalchemy import func, ForeignKey
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
    __tablename__ = "contacto"
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
        nullable=False
    )


class CommerceContactORM(Base):
    '''
    Class to hold the ORM mapping for the 'contact' table
    in the 'onboarding' schema.
    '''
    __tablename__ = "comercio_contacto"
    __table_args__ = {"schema": "onboarding"}

    # Primary key is (comercio_id, contact_id, rol)
    comercio_id: Mapped[int] = mapped_column(
        ForeignKey("onboarding.registro_comercio.id", ondelete="CASCADE"),
        primary_key=True
    )

    contact_id: Mapped[int] = mapped_column(
        ForeignKey("onboarding.contacto.id", ondelete="CASCADE"),
        primary_key=True
    )

    # This establishes the role of the contact in relation to the commerce
    rol: Mapped[str] = mapped_column(
        primary_key=True,
        nullable=False
    )

    # This if this contact is the main contact
    principal: Mapped[bool] = mapped_column(
        nullable=False,
        default=False
    )

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=True
    )


class AccountInfoORM(Base):
    __tablename__ = "cuenta"
    __table_args__ = {"schema": "onboarding"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rut_titular: Mapped[str] = mapped_column(nullable=False)
    nombre_titular: Mapped[str] = mapped_column(nullable=False)
    banco: Mapped[int] = mapped_column(nullable=False)
    tipo_cuenta: Mapped[int] = mapped_column(nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )


class CommerceAccountORM(Base):
    __tablename__ = "cuenta_comercio"
    __table_args__ = {"schema": "onboarding"}
    
    comercio_id: Mapped[int] = mapped_column(
        ForeignKey("onboarding.registro_comercio.id", ondelete="CASCADE"),
        primary_key=True   
    )

    cuenta_id: Mapped[int] = mapped_column(
        ForeignKey("onboarding.cuenta.id", ondelete="CASCADE"),
        primary_key=True   
    )

    # This determines if this account is the "main" account
    principal: Mapped[bool] = mapped_column(
        nullable=False,
        default=False
    )

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=True
    )