from fastapi import FastAPI
from app.controllers import cliente_router, vehiculo_router, orden_router

app = FastAPI(title="Taller Mecánico API")

@app.get("/")
def root():
    return {"message": "API Taller Mecánico funcionando"}

app.include_router(cliente_router)
app.include_router(vehiculo_router)
app.include_router(orden_router)
