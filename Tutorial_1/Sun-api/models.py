from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Has_category(Base):
    __tablename__ = "has_category"

    category = Column(String, primary_key=True, index=True)
    

    items = relationship("New", back_populates="owner")


class New(Base):
    __tablename__ = "new"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    date = Column(String, index=True)
    url = Column(String, index=True)
    media_outlet=Column(String, index=True)
    owner_id = Column(String, ForeignKey("has_category.category"))

    owner = relationship("Has_category", back_populates="items")