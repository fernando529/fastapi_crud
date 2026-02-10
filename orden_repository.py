from sqlalchemy.orm import Session
from app.models.orden import Orden

def get_all(db: Session):
    return db.query(Orden).all()

def create(db: Session, orden: Orden):
    db.add(orden)
    db.commit()
    db.refresh(orden)
    return orden
