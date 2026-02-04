#!/usr/bin/env python3
"""
Скрипт для добавления тестовых данных в базу данных
"""
from app.db.db import SessionLocal, engine
from app.db.models import Category, Book
from app.db.db import Base

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Создание сессии
db = SessionLocal()

try:
    # Очистка существующих данных
    db.query(Book).delete()
    db.query(Category).delete()
    db.commit()
    
    # Создание категорий
    categories_data = [
        {"name": "Художественная литература", "description": "Романы, рассказы, повести"},
        {"name": "Научная литература", "description": "Научные книги и исследования"},
        {"name": "Техническая литература", "description": "Книги по программированию и IT"},
        {"name": "Историческая литература", "description": "Книги по истории"},
    ]
    
    categories = []
    for cat_data in categories_data:
        category = Category(**cat_data)
        db.add(category)
        categories.append(category)
    
    db.commit()
    
    # Обновляем категории, чтобы получить их ID
    for category in categories:
        db.refresh(category)
    
    # Создание книг
    books_data = [
        {
            "title": "Война и мир",
            "description": "Роман-эпопея Льва Толстого",
            "price": 850.50,
            "url": "https://example.com/books/voina-i-mir",
            "category_id": categories[0].id
        },
        {
            "title": "Преступление и наказание",
            "description": "Роман Фёдора Достоевского",
            "price": 720.00,
            "url": "https://example.com/books/prestuplenie-i-nakazanie",
            "category_id": categories[0].id
        },
        {
            "title": "Мастер и Маргарита",
            "description": "Роман Михаила Булгакова",
            "price": 650.75,
            "url": "https://example.com/books/master-i-margarita",
            "category_id": categories[0].id
        },
        {
            "title": "Краткая история времени",
            "description": "Книга Стивена Хокинга о космологии",
            "price": 950.00,
            "url": "https://example.com/books/kratkaya-istoriya-vremeni",
            "category_id": categories[1].id
        },
        {
            "title": "Python для начинающих",
            "description": "Учебник по программированию на Python",
            "price": 1200.00,
            "url": "https://example.com/books/python-dlya-nachinayushchih",
            "category_id": categories[2].id
        },
        {
            "title": "Искусство программирования",
            "description": "Классическая книга Дональда Кнута",
            "price": 2500.00,
            "url": "https://example.com/books/iskusstvo-programmirovaniya",
            "category_id": categories[2].id
        },
        {
            "title": "История России",
            "description": "Подробная история России с древнейших времён",
            "price": 1100.50,
            "url": "https://example.com/books/istoriya-rossii",
            "category_id": categories[3].id
        },
        {
            "title": "1984",
            "description": "Антиутопический роман Джорджа Оруэлла",
            "price": 680.00,
            "url": "https://example.com/books/1984",
            "category_id": categories[0].id
        },
        {
            "title": "FastAPI: современный веб-фреймворк",
            "description": "Руководство по созданию API на FastAPI",
            "price": 1500.00,
            "url": "https://example.com/books/fastapi-guide",
            "category_id": categories[2].id
        },
        {
            "title": "Вторая мировая война",
            "description": "Историческое исследование о Второй мировой войне",
            "price": 1350.00,
            "url": "https://example.com/books/vtoraya-mirovaya-vojna",
            "category_id": categories[3].id
        },
    ]
    
    for book_data in books_data:
        book = Book(**book_data)
        db.add(book)
    
    db.commit()
    
    print("✅ Данные успешно добавлены в базу данных!")
    print(f"   - Создано категорий: {len(categories)}")
    print(f"   - Создано книг: {len(books_data)}")
    
except Exception as e:
    db.rollback()
    print(f"❌ Ошибка при добавлении данных: {e}")
finally:
    db.close()
