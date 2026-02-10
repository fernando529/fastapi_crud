from sqlalchemy.orm import Session
from app.models.vehiculo import Vehiculo

def get_all(db: Session):
    return db.query(Vehiculo).all()

def create(db: Session, vehiculo: Vehiculo):
    db.add(vehiculo)
    db.commit()
    db.refresh(vehiculo)
    return vehiculo
