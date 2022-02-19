from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.config.database import get_db
from typing import List
from src.infra.sqlalchemy.repositorios.pedido import RepositorioPedido

router = APIRouter()

@router.post('/pedidos', status_code=status.HTTP_201_CREATED, response_model=schemas.Pedido)
def fazer_pedido(pedido: schemas.Pedido, session: Session=Depends(get_db)):
    pedido_criado = RepositorioPedido(session).gravar_pedido(pedido)
    return pedido_criado

@router.get('/pedidos/{id}', response_model=schemas.Pedido)
def exibir_pedido(id: int, session: Session=Depends(get_db)):
    try:
        pedido_buscado = RepositorioPedido(session).buscar_pr_id(id)
        return pedido_buscado
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Não existe pedido com o id= {id}'
        )

@router.get('/pedidos/{usuario_id}/compras', response_model=List[schemas.Pedido])
def listar_meus_pedidos_por_usuario_id(usuario_id:int ,session:Session=Depends(get_db)):
    meus_pedidos = RepositorioPedido(session)\
        .listar_meus_pedidos_por_usuario_id(usuario_id)
    return meus_pedidos

@router.get('/pedidos/{usuario_id}/vendas', response_model=List[schemas.Pedido])
def listar_minhas_vendas_por_usuario_id(usuario_id:int, session:Session=Depends(get_db)):
    minhas_vendas = RepositorioPedido(session)\
        .listar_minhas_vendas_por_usuario_id(usuario_id)
    return minhas_vendas
