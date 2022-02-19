from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import router_produto, router_usuario, router_pedido

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

#Routers Produts
app.include_router(router_produto.router)

#Routers Users
app.include_router(router_usuario.router)

#Routers Pedidos
app.include_router(router_pedido.router)