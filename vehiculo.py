from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.database import Base

class Vehiculo(Base):
    __tablename__ = "vehiculos"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
