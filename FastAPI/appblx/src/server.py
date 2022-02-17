#fastapi.Depends busca a conexão com o banco de dados
from fastapi import FastAPI, Depends
#importando tipo Session para cuidar das conexões com o banco de dados
from sqlalchemy.orm import Session
#importando schemas
from src.schemas import schemas
#importando repositório que manipula o banco de dados
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
#importando a conexão com o banco de dados
from src.infra.sqlalchemy.config.database import get_db, criar_db
from typing import List
#import das permissões de CORS
from fastapi.middleware.cors import CORSMiddleware

#criar_db()

app = FastAPI()

#CORS
origins = ['http://localhost']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

#PRODUTOS

@app.post('/criar-produto', response_model=schemas.ProdutoSimples)
def criar_produtos(produto: schemas.Produto, session: Session=Depends(get_db) ):
    produto_criado = RepositorioProduto(session).criar(produto)
    return produto_criado

@app.get('/listar-produtos', response_model=List[schemas.Produto])
def listar_produtos(session:Session=Depends(get_db)):
    produtos = RepositorioProduto(session).listar()
    return produtos

@app.put('/atualizar-produto/{id}', response_model=schemas.ProdutoSimples)
def atualizar_produto(id: int, produto: schemas.Produto, session:Session=Depends(get_db)):
    RepositorioProduto(session).editar(id, produto)
    produto.id = id
    return produto

@app.delete('/deletar-produto/{id}')
def remover_produto(id:int, session:Session=Depends(get_db)):
    RepositorioProduto(session).remover(id)
    return

#USUÁRIOS

@app.post('/signup')
def signup(usuario: schemas.Usuario, session:Session=Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@app.get('/listar-usuarios', response_model=List[schemas.Usuario])
def listar_usuarios(session:Session=Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios