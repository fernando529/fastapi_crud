from sqlalchemy.orm import Session
from app.models.cliente import Cliente
from app.repositories.cliente_repository import create, get_all

def crear_cliente(db: Session, nombre, email, telefono):
    cliente = Cliente(nombre=nombre, email=email, telefono=telefono)
    return create(db, cliente)

def listar_clientes(db: Session):
    return get_all(db)
