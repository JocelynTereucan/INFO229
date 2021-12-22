from sqlalchemy.orm import Session

from . import models, schemas

def get_news(db: Session, skip: int = 0, limit: int = 100): #solo para leer la base de datos
	return db.query(models.News).offset(skip).limit(limit).all() #query para hacer la consulta, devolverá los datos