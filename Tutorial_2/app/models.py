from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship


from .database import Base

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True) #index nos permite acceder mas rapido a los datos
    title = Column(String, index=False) 
    date = Column(Date, index=False)
    url = Column(String, index=False)
    media_outlet=Column(String, index=False)
    category=Column(String, index=False)

#class Has_category(Base):
 #   __tablename__ = "has_category"

  #  category = Column(String, primary_key=True, index=True)
    

   # items = relationship("New", back_populates="owner")


