from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = crud.create_item(db, item=item)
    if db_item:
        raise HTTPException(status_code=400, detail="item already registered")
    return db_item

@app.get("/items/", response_model=list[schemas.Item])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_user(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.post("/items/{item_id}/infos/", response_model=schemas.Info)
def create_info_for_item(item_id: int, info: schemas.InfoCreate, db: Session = Depends(get_db)):
    return crud.create_item_info(db=db, info=info, item_id=item_id)


@app.get("/infos/", response_model=list[schemas.Info])
def read_infos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    infos = crud.get_infos(db, skip=skip, limit=limit)
    return infos


# uvicorn main:app --reload