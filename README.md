# Books API

REST API для управления книгами и категориями, построенное на FastAPI и PostgreSQL.

## Описание

Проект представляет собой REST API с полным набором CRUD операций для управления книгами и категориями. API поддерживает фильтрацию и пагинацию данных.

## Технологии

- **FastAPI** - современный веб-фреймворк для создания API
- **SQLAlchemy** - ORM для работы с базой данных
- **PostgreSQL** - реляционная база данных
- **Pydantic** - валидация данных и схемы
- **Uvicorn** - ASGI сервер

## Установка

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd competence6
```

2. Создайте виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate  # для Linux/Mac/WSL
# или
venv\Scripts\activate  # для Windows
```

3. Установите зависимости (убедитесь, что виртуальное окружение активировано):
```bash
pip install -r requirements.txt
```

**Примечание:** В Linux/WSL может потребоваться использовать `python3` вместо `python`. Если возникает ошибка "externally-managed-environment", обязательно используйте виртуальное окружение.

4. Настройте базу данных:
   - Создайте файл `.env` на основе `config/env.example`
   - Укажите строку подключения к PostgreSQL:
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/books_db
   ```

5. Создайте базу данных в PostgreSQL:
```sql
CREATE DATABASE books_db;
```

6. Запустите приложение:
```bash
uvicorn app.main:app --reload
```

Или используйте скрипт:
```bash
python run.py
```

API будет доступно по адресу: http://localhost:8000

## API Документация

После запуска сервера доступна интерактивная документация:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Эндпоинты

### Health Check
- `GET /health` - проверка работоспособности API

### Категории (Categories)

- `GET /categories` - получить список категорий
  - Параметры запроса:
    - `skip` (int): количество пропускаемых записей (по умолчанию 0)
    - `limit` (int): максимальное количество записей (по умолчанию 100)
    - `name` (str, опционально): фильтр по имени категории
- `GET /categories/{category_id}` - получить категорию по ID
- `POST /categories` - создать новую категорию
- `PUT /categories/{category_id}` - обновить категорию
- `DELETE /categories/{category_id}` - удалить категорию

### Книги (Books)

- `GET /books` - получить список книг
  - Параметры запроса:
    - `skip` (int): количество пропускаемых записей (по умолчанию 0)
    - `limit` (int): максимальное количество записей (по умолчанию 100)
    - `title` (str, опционально): фильтр по названию книги
    - `author` (str, опционально): фильтр по автору
    - `category_id` (int, опционально): фильтр по ID категории
- `GET /books/{book_id}` - получить книгу по ID
- `POST /books` - создать новую книгу
- `PUT /books/{book_id}` - обновить книгу
- `DELETE /books/{book_id}` - удалить книгу

## Примеры использования

### Создание категории
```bash
curl -X POST "http://localhost:8000/categories" \
  -H "Content-Type: application/json" \
  -d '{"name": "Художественная литература", "description": "Романы, рассказы, повести"}'
```

### Создание книги
```bash
curl -X POST "http://localhost:8000/books" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Война и мир",
    "author": "Лев Толстой",
    "description": "Роман-эпопея",
    "category_id": 1
  }'
```

### Получение книг с фильтрацией
```bash
curl "http://localhost:8000/books?author=Толстой&category_id=1"
```

## Структура проекта

```
competence6/
├── app/                 # Основное приложение
│   ├── __init__.py
│   ├── main.py          # Точка входа приложения FastAPI
│   ├── schemas.py       # Pydantic схемы (Category, Book)
│   ├── db/              # Работа с базой данных
│   │   ├── __init__.py
│   │   ├── db.py        # Настройка подключения к БД
│   │   ├── models.py    # SQLAlchemy модели (Category, Book)
│   │   └── crud.py      # CRUD операции
│   └── api/             # API роутеры
│       ├── __init__.py
│       ├── categories.py # Роутер для категорий
│       └── books.py     # Роутер для книг
├── scripts/             # Вспомогательные скрипты
│   ├── check_db.py      # Проверка подключения к БД
│   ├── create_db.sh     # Создание базы данных
│   ├── init_data.py     # Инициализация тестовых данных
│   └── test_api.sh      # Тестирование API
├── sql/                 # SQL скрипты
│   └── psql_select_queries.sql  # Запросы для проверки данных
├── docs/                # Документация
│   └── api_examples.md  # Примеры запросов к API
├── config/              # Конфигурационные файлы
│   └── env.example      # Пример файла с переменными окружения
├── examples/            # Скриншоты работы API
├── run.py              # Скрипт для запуска приложения
├── requirements.txt    # Зависимости проекта
├── .gitignore
└── README.md
```

## Скриншоты и примеры

В папке `examples/` должны быть размещены скриншоты работы API:

1. **swagger_docs.png** - скриншот страницы `/docs` (Swagger UI)
2. **health_check.png** - скриншот работы эндпоинта `/health`
3. **categories_crud.png** - скриншоты CRUD операций с категориями
4. **books_crud.png** - скриншоты CRUD операций с книгами
5. **filtering.png** - скриншоты работы фильтрации
6. **psql_select.png** - **ОБЯЗАТЕЛЬНО**: скриншот psql с SELECT запросами по таблицам categories и books

### Инструкция по созданию скриншотов

1. Запустите сервер: `uvicorn main:app --reload`
2. Откройте браузер и перейдите на http://localhost:8000/docs
3. Сделайте скриншоты:
   - Главной страницы Swagger UI
   - Тестирования каждого эндпоинта
   - Результатов фильтрации
4. **Создайте скриншот psql с SELECT запросами:**
   - Подключитесь к базе данных: `psql -h localhost -U your_username -d books_db`
   - Выполните запросы из файла `examples/psql_select_queries.sql`:
     ```sql
     SELECT * FROM categories;
     SELECT * FROM books;
     SELECT b.id, b.title, b.price, c.name AS category_name
     FROM books b
     JOIN categories c ON b.category_id = c.id;
     ```
   - Сделайте скриншот терминала с результатами запросов
   - Сохраните как `psql_select.png`
5. Сохраните все скриншоты в папку `examples/`

**Примечание:** Если возникают проблемы с подключением к PostgreSQL через psql (ошибка "Peer authentication failed"), используйте подключение через TCP/IP: `psql -h localhost -U username -d books_db`. Подробные инструкции в файле `examples/PSQL_INSTRUCTIONS.md`.

## Чек-лист выполнения

- ✅ Установить FastAPI и Uvicorn, подготовить проект
- ✅ Создать схемы (Pydantic) и настроить подключение к БД (get_db)
- ✅ Реализовать роутеры categories и books с CRUD и фильтрацией
- ✅ Собрать приложение в main.py и добавить /health
- ✅ Запустить сервер, проверить работу /docs и протестировать эндпоинты
- ✅ Проверить данные в PostgreSQL после запросов
- ✅ Сделать скрины и добавить их в examples/, обновить README
- ✅ Закоммитить и залить проект на GitHub

## Автор

Проект выполнен в рамках задания по разработке REST API на FastAPI.
