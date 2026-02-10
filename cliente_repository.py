from sqlalchemy.orm import Session
from app.models.cliente import Cliente

def get_all(db: Session):
    return db.query(Cliente).all()

def create(db: Session, cliente: Cliente):
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente
