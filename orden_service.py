from sqlalchemy.orm import Session
from app.models.orden import Orden
from app.repositories.orden_repository import create, get_all

def crear_orden(db: Session, fallas, vehiculo_id):
    orden = Orden(fallas=fallas, vehiculo_id=vehiculo_id)
    return create(db, orden)

def listar_ordenes(db: Session):
    return get_all(db)
