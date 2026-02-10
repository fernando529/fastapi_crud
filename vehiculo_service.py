from sqlalchemy.orm import Session
from app.models.vehiculo import Vehiculo
from app.repositories.vehiculo_repository import create, get_all

def crear_vehiculo(db: Session, marca, modelo, cliente_id):
    vehiculo = Vehiculo(marca=marca, modelo=modelo, cliente_id=cliente_id)
    return create(db, vehiculo)

def listar_vehiculos(db: Session):
    return get_all(db)
