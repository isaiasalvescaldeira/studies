from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

#CORS é quem filtra as requisições
#Middleware é uma interceptação da requisição antes de chegar no banco de dados
#agora vou configura o cors para que ele aceite requisição de uma origem
origins = [
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Animal(BaseModel):
    id: Optional[str]
    nome: str
    idade: int
    sexo: str
    cor: str
    
#List do tipo animal faz uma validação para que os itens da lista sejam requeridos neste tipo
banco: List[Animal] = []

@app.get('/animais')
def listar_animais():
    return banco

@app.get('/animais/{animal_id}')
def buscar_animal(animal_id: str):
    for animal in banco:
        if animal_id == animal.id:
            return animal
    return {'status': "Erro, animal não encontrado"}

@app.post('/animais')
def criar_animal(animal: Animal):
    animal.id = str(uuid4())
    banco.append(animal)
    return {'status':'tudo certo'}

@app.delete('/animais/{animal_id}')
def deletar_animal(animal_id: str):
    posicao = -1
    for indice, animal in enumerate(banco):
        if animal_id == animal.id:
            posicao = indice
            break
    
    if posicao != -1:
        banco.pop(posicao)
        return {'status': 'animal removido com sucesso'}
    else:
        return {'status': 'animal não encontrado'}

