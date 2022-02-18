from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.config.database import get_db
from typing import List

router = APIRouter()

@router.post('/pedidos')
def fazer_pedido(pedido: schemas.Pedido, session: Session=Depends(get_db)):
    pass

@router.get('/pedidos/{id}')
def exibir_pedido(id: int, session: Session=Depends(get_db)):
    pass

@router.get('/pedidos')
def listar_pedido(session: Session=Depends(get_db)):
    pass