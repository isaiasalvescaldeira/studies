from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)
    senha = Column(String)

    produtos = relationship('Produto', back_populates='usuario')

class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
    
    usuario_id = Column(Integer, ForeignKey('usuario.id', name='fk_usuario'))
    usuario = relationship('Usuario', back_populates='produtos')
