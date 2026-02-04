"""
CRUD операции для работы с базой данных
"""
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.models import Category, Book


# Category CRUD
def get_category(db: Session, category_id: int) -> Optional[Category]:
    """Получить категорию по ID"""
    return db.query(Category).filter(Category.id == category_id).first()


def get_categories(
    db: Session, 
    skip: int = 0, 
    limit: int = 100,
    name: Optional[str] = None
) -> List[Category]:
    """Получить список категорий с фильтрацией"""
    query = db.query(Category)
    if name:
        query = query.filter(Category.name.ilike(f"%{name}%"))
    return query.offset(skip).limit(limit).all()


def create_category(db: Session, category_data: dict) -> Category:
    """Создать новую категорию"""
    db_category = Category(**category_data)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def update_category(db: Session, category_id: int, category_data: dict) -> Optional[Category]:
    """Обновить категорию"""
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category:
        for field, value in category_data.items():
            setattr(db_category, field, value)
        db.commit()
        db.refresh(db_category)
    return db_category


def delete_category(db: Session, category_id: int) -> bool:
    """Удалить категорию"""
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
        return True
    return False


# Book CRUD
def get_book(db: Session, book_id: int) -> Optional[Book]:
    """Получить книгу по ID"""
    return db.query(Book).filter(Book.id == book_id).first()


def get_books(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    title: Optional[str] = None,
    category_id: Optional[int] = None
) -> List[Book]:
    """Получить список книг с фильтрацией"""
    query = db.query(Book)
    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if category_id:
        query = query.filter(Book.category_id == category_id)
    return query.offset(skip).limit(limit).all()


def create_book(db: Session, book_data: dict) -> Book:
    """Создать новую книгу"""
    db_book = Book(**book_data)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def update_book(db: Session, book_id: int, book_data: dict) -> Optional[Book]:
    """Обновить книгу"""
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        for field, value in book_data.items():
            setattr(db_book, field, value)
        db.commit()
        db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int) -> bool:
    """Удалить книгу"""
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
        return True
    return False
