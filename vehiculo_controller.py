from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.services.vehiculo_service import (
    listar_vehiculos,
    crear_vehiculo
)

router = APIRouter(prefix="/vehiculos", tags=["Vehiculos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return listar_vehiculos(db)

@router.post("/")
def crear(marca: str, modelo: str, cliente_id: int, db: Session = Depends(get_db)):
    return crear_vehiculo(db, marca, modelo, cliente_id)

