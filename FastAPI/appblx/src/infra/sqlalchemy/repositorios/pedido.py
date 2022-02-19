from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioPedido():
    def __init__(self, session: Session):
        self.session = session

    def gravar_pedido(self, pedido:schemas.Pedido):
        sessionAddPedido = models.Pedido(
            quantidade = pedido.quantidade,
            tipo_entrega = pedido.tipo_entrega,
            local_entrega = pedido.local_entrega,
            observacoes = pedido.observacoes,
            usuario_id = pedido.usuario_id,
            produto_id = pedido.produto_id
            )
        
        self.session.add(sessionAddPedido)
        self.session.commit()
        self.session.refresh(sessionAddPedido)

        return sessionAddPedido

    def buscar_pr_id(self, id:int):
        query_pedido = select(models.Pedido)\
            .where(models.Pedido.id == id)
        pedido = self.session.execute(query_pedido).first()
        #o resultado de uma consulta é sempre uma lista de objetos
        #o indice 0 é para pegar o primeiro objeto de cada lista
        return pedido[0]

    def listar_meus_pedidos_por_usuario_id(self, usuario_id:int):
        query_pedidos_usuario = select(models.Pedido)\
            .where(models.Pedido.usuario_id == usuario_id)
        pedidos_usuario = self.session.execute(query_pedidos_usuario).scalars().all()
        return pedidos_usuario

    def listar_minhas_vendas_por_usuario_id(self, usuario_id:int):

        #seleciona a tabela Pedido para retornar os atributos da mesma
        #faz um join entre as tabelas Pedido e Produto
        #pega as linhas na tabela de Pedido onde Produto.usuario_id = usuario_id que chegou na url
        query_vendas_usuario = select(models.Pedido)\
            .join_from(models.Pedido, models.Produto)\
                .where(models.Produto.usuario_id == usuario_id)
        #scalars() evita de retornar uma lista de objetos Pedido
        vendas_usuario = self.session.execute(query_vendas_usuario).scalars().all()
        return vendas_usuario