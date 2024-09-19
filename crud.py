from sqlalchemy.orm import Session

from . import models, schemas


def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def get_items_by_info_context(db: Session, info_context: str):
    return db.query(models.Item).join(models.Item.infos).filter(models.Info.context == info_context).all()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_infos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Info).offset(skip).limit(limit).all()


def create_item_info(db: Session, info: schemas.InfoCreate, item_id: int):
    db_info = models.Info(**info.model_dump(), item_id=item_id)
    db.add(db_info)
    db.commit()
    db.refresh(db_info)
    return db_info