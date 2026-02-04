from fastapi import FastAPI
from app.db.db import engine, Base
from app.api import categories, books

# Создание таблиц в БД
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Books API",
    description="API для управления книгами и категориями",
    version="1.0.0"
)

# Подключение роутеров
app.include_router(categories.router)
app.include_router(books.router)


@app.get("/health")
def health_check():
    """Проверка здоровья приложения"""
    return {"status": "ok", "message": "API работает корректно"}


@app.get("/")
def root():
    """Корневой эндпоинт"""
    return {
        "message": "Добро пожаловать в Books API",
        "docs": "/docs",
        "health": "/health"
    }
