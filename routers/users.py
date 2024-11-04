from pydantic import BaseModel

# Esquema para el Usuario
class UsuarioCreate(BaseModel):
    username: str
    password: str

class UsuarioResponse(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
