from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal


# Category Schemas
class CategoryBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = None


class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True


# Book Schemas
class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    price: Optional[Decimal] = None
    url: Optional[str] = Field(None, max_length=500)
    category_id: int


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    price: Optional[Decimal] = None
    url: Optional[str] = Field(None, max_length=500)
    category_id: Optional[int] = None


class Book(BookBase):
    id: int
    category: Optional[Category] = None

    class Config:
        from_attributes = True
