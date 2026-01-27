from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, joinedload
from typing import List, Optional
from app import schemas, models
from app.database import get_db

router = APIRouter(prefix="/books", tags=["books"])


@router.post("/", response_model=schemas.Book, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """Создать новую книгу"""
    # Проверка существования категории
    category = db.query(models.Category).filter(models.Category.id == book.category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    # Загружаем категорию для ответа
    db_book = db.query(models.Book).options(joinedload(models.Book.category)).filter(models.Book.id == db_book.id).first()
    return db_book


@router.get("/", response_model=List[schemas.Book])
def get_books(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    title: Optional[str] = Query(None, description="Фильтр по названию книги"),
    author: Optional[str] = Query(None, description="Фильтр по автору"),
    category_id: Optional[int] = Query(None, description="Фильтр по ID категории"),
    db: Session = Depends(get_db)
):
    """Получить список книг с фильтрацией"""
    query = db.query(models.Book).options(joinedload(models.Book.category))
    
    if title:
        query = query.filter(models.Book.title.ilike(f"%{title}%"))
    
    if author:
        query = query.filter(models.Book.author.ilike(f"%{author}%"))
    
    if category_id:
        query = query.filter(models.Book.category_id == category_id)
    
    books = query.offset(skip).limit(limit).all()
    return books


@router.get("/{book_id}", response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """Получить книгу по ID"""
    book = db.query(models.Book).options(joinedload(models.Book.category)).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book


@router.put("/{book_id}", response_model=schemas.Book)
def update_book(
    book_id: int,
    book: schemas.BookUpdate,
    db: Session = Depends(get_db)
):
    """Обновить книгу"""
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    
    # Проверка существования категории, если она обновляется
    if book.category_id and book.category_id != db_book.category_id:
        category = db.query(models.Category).filter(models.Category.id == book.category_id).first()
        if not category:
            raise HTTPException(status_code=404, detail="Категория не найдена")
    
    update_data = book.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_book, field, value)
    
    db.commit()
    db.refresh(db_book)
    # Загружаем категорию для ответа
    db_book = db.query(models.Book).options(joinedload(models.Book.category)).filter(models.Book.id == db_book.id).first()
    return db_book


@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Удалить книгу"""
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    
    db.delete(db_book)
    db.commit()
    return None

