from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db
from typing import List

router = APIRouter()

#USUÁRIOS

@router.post('/signup')
def signup(usuario: schemas.Usuario, session:Session=Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@router.get('/usuarios', response_model=List[schemas.Usuario])
def listar_usuarios(session:Session=Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios