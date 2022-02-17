from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
from src.schemas import schemas

class RepositorioSerie:
    def __init__(self, db:Session):
        self.db = db

    def criar(self, serie: schemas.Serie):
        db_serie = models.Serie(
            titulo = serie.titulo,
            ano = serie.ano,
            genero = serie.genero,
            qtd_temporadas = serie.qtd_temporadas
        )
        self.db.add(db_serie)
        self.db.commit()
        self.db.refresh(db_serie)
        return db_serie

    def listar(self):
        series = self.db.query(models.Serie).all()
        return series

    def obter(self, id_serie:int):
        statment = select(models.Serie).filter_by(id=id_serie)
        serie = self.db.execute(statment).one()
        return serie

    def remover(self, id_serie:int):
        statment = delete(models.Serie).where(models.Serie.id == id_serie)
        self.db.execute(statment)
        self.db.commit()
    
    def obter_por_titulo(self, titulo_serie:str):
        statment = select(models.Serie).where(models.Serie.titulo==titulo_serie)
        serie_por_titulo = self.db.execute(statment).one()
        return serie_por_titulo