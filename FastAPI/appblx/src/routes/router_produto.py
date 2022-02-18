from fastapi import APIRouter
#fastapi.Depends busca a conexão com o banco de dados
from fastapi import Depends
#importando tipo Session para cuidar das conexões com o banco de dados
from sqlalchemy.orm import Session
#importando schemas
from src.schemas import schemas
#importando repositório que manipula o banco de dados
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
#importando a conexão com o banco de dados
from src.infra.sqlalchemy.config.database import get_db
from typing import List

router = APIRouter()

#PRODUTOS

@router.post('/criar-produto', response_model=schemas.ProdutoSimples)
def criar_produtos(produto: schemas.Produto, session: Session=Depends(get_db) ):
    produto_criado = RepositorioProduto(session).criar(produto)
    return produto_criado

@router.get('/listar-produtos', response_model=List[schemas.Produto])
def listar_produtos(session:Session=Depends(get_db)):
    produtos = RepositorioProduto(session).listar()
    return produtos

@router.put('/atualizar-produto/{id}', response_model=schemas.ProdutoSimples)
def atualizar_produto(id: int, produto: schemas.Produto, session:Session=Depends(get_db)):
    RepositorioProduto(session).editar(id, produto)
    produto.id = id
    return produto

@router.delete('/deletar-produto/{id}')
def remover_produto(id:int, session:Session=Depends(get_db)):
    RepositorioProduto(session).remover(id)
    return