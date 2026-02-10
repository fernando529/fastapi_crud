from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.services.cliente_service import crear_cliente, listar_clientes

router = APIRouter(prefix="/clientes", tags=["Clientes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return listar_clientes(db)

@router.post("/")
def crear(nombre: str, email: str, telefono: str, db: Session = Depends(get_db)):
    return crear_cliente(db, nombre, email, telefono)
