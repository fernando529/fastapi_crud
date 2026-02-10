from pydantic import BaseModel

class ClienteBase(BaseModel):
    nombre: str
    email: str
    telefono: str

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id: int

    class Config:
        from_attributes = True
