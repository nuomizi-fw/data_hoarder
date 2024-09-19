from pydantic import BaseModel


class InfoBase(BaseModel):
    id: int
    type: str | None = None
    context: str | None = None

class InfoCreate(InfoBase):
    item_id: int

class Info(InfoBase):
    id: int

    class Config:
        orm_mode = True

class ItemBase(BaseModel):
    id: int
    infos: list[Info]

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    infos: list[Info] = []

    class Config:
        orm_mode = True
