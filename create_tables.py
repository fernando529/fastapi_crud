from app.database.database import engine,Base
from app.models.cliente import Cliente
from app.models.vehiculo import Vehiculo
from app.models.orden import OrdenServicio

Base.metadata.create_all(bind=engine)

print(" Tablas creadas correctamente")
