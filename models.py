from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

# class Info(BaseModel):
#     type: str
#     context: str
# 
# class Item(BaseModel):
#     id: int
#     infos: list[Info]


class Info(Base):
    __tablename__ = "infos"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, unique=True, index=True)
    context = Column(String)
    item_id = Column(Integer, ForeignKey("items.id"))

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    infos = relationship("Info", back_populates="items")
    