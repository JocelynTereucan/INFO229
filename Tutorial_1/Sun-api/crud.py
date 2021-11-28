from sqlalchemy.orm import Session

from . import models, schemas


def Has_category(db:sun, category:str);
    return db.query(models.Has_category).filter(models.Has_category.category == category).first()



def get_new(db:sun, skip: int = 0, limit: int = 100):
    return db.query(models.New).offset(skip).limit(limit).all()


def create_user_item(db:sun, item: schemas.NewCreate, category: str):
    db_item = models.New(**item.dict(), owner_id=category)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
