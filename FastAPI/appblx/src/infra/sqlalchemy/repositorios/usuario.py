from sqlalchemy.orm import Session
from sqlalchemy import select
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioUsuario():
    
    def __init__(self, session: Session):
        self.session = session
    
    #usuario é um tipo Schema
    def criar(self, usuario: schemas.Usuario):
        #db_usuario vai receber uma "ficha de cadastro(models.Usuario)"
        #que vai receber os dados vindos do schema
        db_usuario = models.Usuario(
            nome = usuario.nome,
            senha = usuario.senha,
            telefone = usuario.telefone
        )
    
        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh(db_usuario)

        return db_usuario
    
    def listar(self):
        stmt = select(models.Usuario)
        usuarios = self.session.execute(stmt).scalars().all()
        return usuarios
    
    def editar(self):

        pass

    def remover(self):
        pass
