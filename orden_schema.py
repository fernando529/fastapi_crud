from pydantic import BaseModel

class OrdenBase(BaseModel):
    fallas: str
    vehiculo_id: int

class OrdenCreate(OrdenBase):
    pass

class OrdenResponse(OrdenBase):
    id: int

    class Config:
        from_attributes = True
