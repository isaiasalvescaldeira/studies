#fastapi.Depends busca a conexão com o banco de dados
from fastapi import Depends, APIRouter, HTTPException, status
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

@router.post('/produtos', response_model=schemas.ProdutoSimples)
def criar_produtos(produto: schemas.Produto, session: Session=Depends(get_db) ):
    produto_criado = RepositorioProduto(session).criar(produto)
    return produto_criado

@router.get('/produtos', response_model=List[schemas.ProdutoSimples])
def listar_produtos(session:Session=Depends(get_db)):
    produtos = RepositorioProduto(session).listar()
    return produtos

@router.get('/produtos/{id}')
def exibir_produto(id: int, session: Session = Depends(get_db)):
    produto = RepositorioProduto(session).buscarPorId(id)
    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Não existe produto com o id: {id}'
            )
    return produto

@router.put('/produtos/{id}', response_model=schemas.ProdutoSimples)
def atualizar_produto(id: int, produto: schemas.Produto, session:Session=Depends(get_db)):
    RepositorioProduto(session).editar(id, produto)
    produto.id = id
    return produto

@router.delete('/produtos/{id}')
def remover_produto(id:int, session:Session=Depends(get_db)):
    RepositorioProduto(session).remover(id)
    return