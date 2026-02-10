from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.database import Base

class Orden(Base):
    __tablename__ = "ordenes"

    id = Column(Integer, primary_key=True, index=True)
    fallas = Column(String, nullable=False)
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"))
