from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import criar_db, get_db
from src.schemas import schemas
from src.infra.sqlalchemy.repository.serie import RepositorioSerie

#criar a base de dados
criar_db()

app = FastAPI()

@app.post('/criar-series')
def criar_series(serie: schemas.Serie, db:Session=Depends(get_db)):
    serie_criada = RepositorioSerie(db).criar(serie)
    return serie_criada

@app.get('/listar-series')
def listar_series(db:Session=Depends(get_db)):
    series = RepositorioSerie(db).listar()
    return series

@app.get('/obter-serie/{id_serie}')
def obter_serie(id_serie:int, db:Session=Depends(get_db)):
    serie = RepositorioSerie(db).obter(id_serie)
    return serie

@app.delete('/deletar-serie/{id_serie}')
def deletar_serie(id_serie:int, db:Session=Depends(get_db)):
    serie = RepositorioSerie(db).remover(id_serie)
    return {"msg":"serie removida"}

@app.get('/obter-serie-por-titulo/{titulo_serie}')
def obter_serie_por_titulo(titulo_serie:str, db:Session=Depends(get_db)):
    serie = RepositorioSerie(db).obter_por_titulo(titulo_serie)
    return serie