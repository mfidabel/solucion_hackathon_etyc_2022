from sqlalchemy.orm import Session
from . import models, schemas


def get_cuenta(db: Session, id: int):
    return db.query(models.Cuenta).filter(models.Cuenta.id == id).first()


def get_cuenta_by_numero_celular(db: Session, numero_celular: int):
    return db.query(models.Cuenta).filter(models.Cuenta.numero_celular == numero_celular).first()


def create_cuenta(db: Session, cuenta: schemas.CuentaCreate):
    db_cuenta = models.Cuenta(numero_celular=cuenta.numero_celular,
                              nombre_beneficiario=cuenta.nombre_beneficiario,
                              numero_cuenta=cuenta.numero_cuenta,
                              numero_cedula=cuenta.numero_cedula,
                              banco_receptor=cuenta.banco_receptor)
    db.add(db_cuenta)
    db.commit()
    db.refresh(db_cuenta)
    return db_cuenta