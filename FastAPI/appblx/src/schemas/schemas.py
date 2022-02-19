from pydantic import BaseModel
from typing import Optional, List

class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: float
    disponivel: bool = False

    class Config:
        orm_mode = True 

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    senha: str
    telefone: str
    produtos: List[ProdutoSimples] = []

    class Config:
        orm_mode=True

class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str

    class Config:
        orm_mode=True

class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    descricao: str
    preco: float
    disponivel: bool = False
    usuario_id: Optional[int]
    usuario: Optional[UsuarioSimples]

    class Config:
        orm_mode=True


class Pedido(BaseModel):
    id: Optional[int] = None
    quantidade: int
    tipo_entrega: str
    local_entrega: Optional[str] = ''
    observacoes: Optional[str] = 'Sem Observações'

    usuario_id: Optional[int]
    produto_id: Optional[int]

    usuario: Optional[UsuarioSimples]
    produto: Optional[ProdutoSimples]

    class Config:
        orm_mode=True