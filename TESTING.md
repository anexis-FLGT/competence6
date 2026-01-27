# Инструкция по тестированию API

## Подготовка

1. Убедитесь, что PostgreSQL запущен и создана база данных `books_db`
2. Создайте файл `.env` с настройками подключения:
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/books_db
   ```
3. Запустите сервер:
   ```bash
   uvicorn main:app --reload
   ```
   или
   ```bash
   python run.py
   ```

## Тестирование через Swagger UI

1. Откройте браузер и перейдите на http://localhost:8000/docs
2. Протестируйте все эндпоинты через интерактивный интерфейс

## Тестирование через curl

### 1. Health Check
```bash
curl http://localhost:8000/health
```

### 2. Создание категорий
```bash
# Создать первую категорию
curl -X POST "http://localhost:8000/categories" \
  -H "Content-Type: application/json" \
  -d '{"name": "Художественная литература", "description": "Романы, рассказы, повести"}'

# Создать вторую категорию
curl -X POST "http://localhost:8000/categories" \
  -H "Content-Type: application/json" \
  -d '{"name": "Научная литература", "description": "Научные книги и исследования"}'
```

### 3. Получение списка категорий
```bash
# Получить все категории
curl http://localhost:8000/categories

# Фильтрация по имени
curl "http://localhost:8000/categories?name=Художественная"
```

### 4. Получение категории по ID
```bash
curl http://localhost:8000/categories/1
```

### 5. Обновление категории
```bash
curl -X PUT "http://localhost:8000/categories/1" \
  -H "Content-Type: application/json" \
  -d '{"name": "Художественная литература", "description": "Обновленное описание"}'
```

### 6. Создание книг
```bash
# Создать первую книгу
curl -X POST "http://localhost:8000/books" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Война и мир",
    "author": "Лев Толстой",
    "description": "Роман-эпопея о войне 1812 года",
    "category_id": 1
  }'

# Создать вторую книгу
curl -X POST "http://localhost:8000/books" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Преступление и наказание",
    "author": "Федор Достоевский",
    "description": "Психологический роман",
    "category_id": 1
  }'

# Создать третью книгу
curl -X POST "http://localhost:8000/books" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Краткая история времени",
    "author": "Стивен Хокинг",
    "description": "Популярная книга о космологии",
    "category_id": 2
  }'
```

### 7. Получение списка книг
```bash
# Получить все книги
curl http://localhost:8000/books

# Фильтрация по автору
curl "http://localhost:8000/books?author=Толстой"

# Фильтрация по названию
curl "http://localhost:8000/books?title=Война"

# Фильтрация по категории
curl "http://localhost:8000/books?category_id=1"

# Комбинированная фильтрация
curl "http://localhost:8000/books?author=Толстой&category_id=1"

# Пагинация
curl "http://localhost:8000/books?skip=0&limit=10"
```

### 8. Получение книги по ID
```bash
curl http://localhost:8000/books/1
```

### 9. Обновление книги
```bash
curl -X PUT "http://localhost:8000/books/1" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Война и мир",
    "author": "Лев Николаевич Толстой",
    "description": "Обновленное описание",
    "category_id": 1
  }'
```

### 10. Удаление книги
```bash
curl -X DELETE http://localhost:8000/books/1
```

### 11. Удаление категории
```bash
# Удаление категории (только если в ней нет книг)
curl -X DELETE http://localhost:8000/categories/2
```

## Проверка данных в PostgreSQL

После выполнения запросов проверьте данные в базе:

```sql
-- Подключитесь к базе данных
psql -U user -d books_db

-- Просмотр категорий
SELECT * FROM categories;

-- Просмотр книг
SELECT * FROM books;

-- Просмотр книг с категориями
SELECT b.id, b.title, b.author, c.name as category_name
FROM books b
JOIN categories c ON b.category_id = c.id;
```

## Ожидаемые результаты

- Все CRUD операции должны работать корректно
- Фильтрация должна возвращать правильные результаты
- Валидация должна работать (попробуйте создать категорию с пустым именем)
- Ошибки должны возвращаться с правильными кодами статуса (404, 400 и т.д.)

