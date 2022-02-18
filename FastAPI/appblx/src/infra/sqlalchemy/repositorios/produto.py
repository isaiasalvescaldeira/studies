from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import update, delete, select

#Este arquivo é onde fica todas as querys do meu banco de dados(CRUD)
#com os métodos do ORM SQLAlchemy

#Sempre que vc esta no repositorio, vc está lidando com modelos,
#quem esta indo e vindo são modelos, e não os schemas


class RepositorioProduto():

    def __init__(self, session: Session):
        self.session = session


    #Recebe o schema do produto, a partir desse schema ele cria/converte em um 
    #db_produto que é um model e manda guardar no banco de dados 
    # e retorna pra uem chamou ele
    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(
            nome=produto.nome,
            descricao=produto.descricao,
            preco = produto.preco,
            disponivel = produto.disponivel,
            usuario_id = produto.usuario_id
        )

        #pegando o banco do self e adicionando o db_produto no banco de dados
        self.session.add(db_produto)
        #confirmando transação
        self.session.commit()
        #agora o db vai atualizar db_produto
        self.session.refresh(db_produto)
        #agora ele vai retornar o db_produto atualizado com o novo produto
        return db_produto

    def buscarPorId(self, id:int):
        query_produto = select(models.Produto)\
            .where(models.Produto.id == id)
        produto = self.session.execute(query_produto).first()
        return produto

    def listar(self):
        produtos = self.session.query(models.Produto).all()
        return produtos

    def editar(self, id: int, produto: schemas.Produto):
        update_stmt = update(models.Produto)\
            .where(models.Produto.id == id)\
                .values(
                    nome=produto.nome,
                    descricao=produto.descricao,
                    preco = produto.preco,
                    disponivel = produto.disponivel
                )
        
        self.session.execute(update_stmt)
        self.session.commit()

    def remover(self, id:int):
        delete_stmt = delete(models.Produto).where(models.Produto.id == id)

        self.session.execute(delete_stmt)
        self.session.commit()
        
