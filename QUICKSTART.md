# Быстрый старт

## 1. Установка зависимостей

**Важно:** Сначала создайте виртуальное окружение (особенно для Linux/WSL):

```bash
# Создание виртуального окружения
python3 -m venv venv

# Активация виртуального окружения
source venv/bin/activate  # для Linux/Mac/WSL
# или
venv\Scripts\activate  # для Windows

# Установка зависимостей
pip install -r requirements.txt
```

## 2. Настройка базы данных

1. Установите и запустите PostgreSQL
2. Создайте базу данных:
```sql
CREATE DATABASE books_db;
```

3. Создайте файл `.env` в корне проекта:
```
DATABASE_URL=postgresql://your_user:your_password@localhost:5432/books_db
```

## 3. Запуск приложения

**Убедитесь, что виртуальное окружение активировано!**

```bash
# Если не активировано, активируйте:
source venv/bin/activate  # для Linux/Mac/WSL

# Запуск сервера
uvicorn main:app --reload
```

или

```bash
python run.py
```

## 4. Проверка работы

1. Откройте браузер: http://localhost:8000/docs
2. Проверьте `/health`: http://localhost:8000/health
3. Протестируйте эндпоинты через Swagger UI

## 5. Создание скриншотов

Сделайте скриншоты следующих страниц и сохраните в папку `examples/`:

1. **swagger_docs.png** - главная страница `/docs`
2. **health_check.png** - результат запроса `/health`
3. **create_category.png** - создание категории
4. **get_categories.png** - список категорий
5. **create_book.png** - создание книги
6. **get_books.png** - список книг
7. **filtering.png** - работа фильтрации
8. **postgresql_data.png** - данные в PostgreSQL

## 6. Загрузка на GitHub

Следуйте инструкциям в файле `DEPLOYMENT.md`

