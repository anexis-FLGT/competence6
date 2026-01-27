from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app import schemas, models
from app.database import get_db

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("/", response_model=schemas.Category, status_code=201)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    """Создать новую категорию"""
    # Проверка на уникальность имени
    db_category = db.query(models.Category).filter(models.Category.name == category.name).first()
    if db_category:
        raise HTTPException(status_code=400, detail="Категория с таким именем уже существует")
    
    db_category = models.Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


@router.get("/", response_model=List[schemas.Category])
def get_categories(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    name: Optional[str] = Query(None, description="Фильтр по имени категории"),
    db: Session = Depends(get_db)
):
    """Получить список категорий с фильтрацией"""
    query = db.query(models.Category)
    
    if name:
        query = query.filter(models.Category.name.ilike(f"%{name}%"))
    
    categories = query.offset(skip).limit(limit).all()
    return categories


@router.get("/{category_id}", response_model=schemas.Category)
def get_category(category_id: int, db: Session = Depends(get_db)):
    """Получить категорию по ID"""
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return category


@router.put("/{category_id}", response_model=schemas.Category)
def update_category(
    category_id: int,
    category: schemas.CategoryUpdate,
    db: Session = Depends(get_db)
):
    """Обновить категорию"""
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    
    # Проверка на уникальность имени, если оно обновляется
    if category.name and category.name != db_category.name:
        existing_category = db.query(models.Category).filter(
            models.Category.name == category.name
        ).first()
        if existing_category:
            raise HTTPException(status_code=400, detail="Категория с таким именем уже существует")
    
    update_data = category.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_category, field, value)
    
    db.commit()
    db.refresh(db_category)
    return db_category


@router.delete("/{category_id}", status_code=204)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    """Удалить категорию"""
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    
    # Проверка на наличие книг в категории
    books_count = db.query(models.Book).filter(models.Book.category_id == category_id).count()
    if books_count > 0:
        raise HTTPException(
            status_code=400,
            detail=f"Невозможно удалить категорию: в ней находится {books_count} книг(и)"
        )
    
    db.delete(db_category)
    db.commit()
    return None

