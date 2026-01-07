from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, UniqueConstraint
from application.data.db import Base

class CuentaORM(Base):
    __tablename__ = "cuentas"
    __table_args__ = {"schema": "onboarding_extras"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tipo_cuenta: Mapped[str] = mapped_column(nullable=False)
    codigo_tipo: Mapped[int] = mapped_column(nullable=False, unique=True)



class BancoORM(Base):
    __tablename__ = "bancos"
    __table_args__ = {"schema": "onboarding_extras"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre_banco: Mapped[str] = mapped_column(nullable=False)
    codigo_banco: Mapped[int] = mapped_column(nullable=False, unique=True)


class RegionORM(Base):
    __tablename__ = "regiones"
    __table_args__ = {"schema": "onboarding_extras"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre_region: Mapped[str] = mapped_column(nullable=False)
    codigo_region: Mapped[int] = mapped_column(nullable=False, unique=True)


class ComunaORM(Base):
    __tablename__ = "comunas"
    __table_args__ = (
        UniqueConstraint("codigo_region", "codigo_comuna"),
        {"schema": "onboarding_extras"}
        )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    codigo_region: Mapped[int] = mapped_column(
        ForeignKey("onboarding_extras.regiones.codigo_region", ondelete="CASCADE"),
        primary_key=False
    )

    codigo_comuna: Mapped[int] = mapped_column(nullable=False)
    nombre_comuna: Mapped[str] = mapped_column(nullable=False)
