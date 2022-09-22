from sqlalchemy import Column, Integer, String

from .database import Base


class Cuenta(Base):
    __tablename__ = "cuentas"

    id = Column(Integer, primary_key=True, index=True)
    numero_celular = Column(Integer, unique=True, index=True)
    nombre_beneficiario = Column(String)
    numero_cuenta = Column(String)
    numero_cedula = Column(Integer)
    banco_receptor = Column(String)

