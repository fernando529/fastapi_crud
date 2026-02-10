from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.services.orden_service import crear_orden, listar_ordenes

router = APIRouter(prefix="/ordenes", tags=["Ordenes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return listar_ordenes(db)

@router.post("/")
def crear(fallas: str, vehiculo_id: int, db: Session = Depends(get_db)):
    return crear_orden(db, fallas, vehiculo_id)
