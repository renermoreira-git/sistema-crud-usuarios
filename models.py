from pydantic import BaseModel


class Usuario(BaseModel):
    nome: str
    idade: int
    cidade: str

class UsuarioUpdate(BaseModel):
    nome: str | None = None
    idade: int | None = None
    cidade: str | None = None