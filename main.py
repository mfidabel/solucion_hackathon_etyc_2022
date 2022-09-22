from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/cuentas/", response_model=schemas.Cuenta)
def create_cuenta(cuenta: schemas.CuentaCreate, db: Session = Depends(get_db)):
    db_cuenta = crud.get_cuenta_by_numero_celular(db, numero_celular=cuenta.numero_celular)

    if db_cuenta:
        raise HTTPException(status_code=400, detail="Número de Celular ya Registrado")

    return crud.create_cuenta(db=db, cuenta=cuenta)


@app.get("/cuentas/{numero_celular}", response_model=schemas.Cuenta)
def obtener_cuenta_por_celular(numero_celular: int, db: Session = Depends(get_db)):
    db_cuenta = crud.get_cuenta_by_numero_celular(db, numero_celular=numero_celular)

    if not db_cuenta:
        raise HTTPException(status_code=400, detail="Número de Celular no está Registrado")

    return db_cuenta

