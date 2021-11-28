from typing import List, Optional


from pydantic import BaseModel


class NewBase(BaseModel):
    title: str
    date: str 
    url: str
    media_outlet: str


class NewCreate(NewBase):
    pass



class New(NewBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True



class CategoryBase(BaseModel):





class CategoryCreate(CategoryBase):

    



class Category(CategoryBase):
    category: str
    items: List[New] = []

    class Config:
        orm_mode = True
