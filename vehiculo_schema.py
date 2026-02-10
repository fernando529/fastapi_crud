from pydantic import BaseModel

class VehiculoBase(BaseModel):
    marca: str
    modelo: str
    cliente_id: int

class VehiculoCreate(VehiculoBase):
    pass

class VehiculoResponse(VehiculoBase):
    id: int

    class Config:
        from_attributes = True
