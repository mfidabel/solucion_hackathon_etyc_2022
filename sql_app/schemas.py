from pydantic import BaseModel


class CuentaBase(BaseModel):
    numero_celular: int
    nombre_beneficiario: str
    numero_cuenta: str
    numero_cedula: int
    banco_receptor: str


class CuentaCreate(CuentaBase):
    pass


class Cuenta(CuentaBase):
    id: int

    class Config:
        orm_mode = True


