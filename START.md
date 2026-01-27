# Инструкция по запуску

## ✅ Текущий статус

- ✅ Виртуальное окружение создано и зависимости установлены
- ✅ База данных `books_db` создана
- ✅ Таблицы `categories` и `books` уже существуют
- ✅ Подключение к базе данных работает

## 🚀 Запуск сервера

1. Активируйте виртуальное окружение (если еще не активировано):
   ```bash
   source venv/bin/activate
   ```

2. Запустите сервер:
   ```bash
   uvicorn main:app --reload
   ```
   
   или
   
   ```bash
   python run.py
   ```

3. Сервер будет доступен по адресу: **http://localhost:8000**

## 📚 Тестирование API

1. **Откройте Swagger UI**: http://localhost:8000/docs
   - Здесь вы можете интерактивно тестировать все эндпоинты

2. **Проверьте health check**: http://localhost:8000/health
   - Должен вернуть: `{"status": "ok", "message": "API работает корректно"}`

3. **Протестируйте эндпоинты**:
   - Создайте категорию через POST /categories
   - Создайте книгу через POST /books
   - Используйте фильтрацию через GET /books?author=Толстой
   - И т.д.

## 📸 Создание скриншотов

После тестирования сделайте скриншоты и сохраните в папку `examples/`:

1. `swagger_docs.png` - главная страница /docs
2. `health_check.png` - результат /health
3. `create_category.png` - создание категории
4. `get_categories.png` - список категорий
5. `create_book.png` - создание книги
6. `get_books.png` - список книг
7. `filtering.png` - работа фильтрации
8. `postgresql_data.png` - данные в PostgreSQL

## 🔍 Проверка данных в PostgreSQL

```bash
# Подключитесь к базе данных
psql -U octagon -d books_db

# Или через sudo
sudo -u postgres psql -d books_db

# Просмотр категорий
SELECT * FROM categories;

# Просмотр книг
SELECT * FROM books;

# Просмотр книг с категориями
SELECT b.id, b.title, b.author, c.name as category_name
FROM books b
JOIN categories c ON b.category_id = c.id;
```

## 📤 Загрузка на GitHub

После создания скриншотов следуйте инструкциям в `DEPLOYMENT.md`

