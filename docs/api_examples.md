# Примеры запросов к Books API

## Базовый URL
```
http://127.0.0.1:8000
```

---

## Health Check

### Проверка работоспособности API
```bash
curl http://127.0.0.1:8000/health
```

**Ответ:**
```json
{
  "status": "ok",
  "message": "API работает корректно"
}
```

---

## Категории (Categories)

### 1. Получить список всех категорий
```bash
curl http://127.0.0.1:8000/categories
```

### 2. Получить список категорий с пагинацией
```bash
curl "http://127.0.0.1:8000/categories?skip=0&limit=10"
```

### 3. Поиск категорий по имени
```bash
curl "http://127.0.0.1:8000/categories?name=Художественная"
```

### 4. Получить категорию по ID
```bash
curl http://127.0.0.1:8000/categories/1
```

### 5. Создать новую категорию
```bash
curl -X POST "http://127.0.0.1:8000/categories" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Детективы",
    "description": "Детективные романы и триллеры"
  }'
```

### 6. Обновить категорию
```bash
curl -X PUT "http://127.0.0.1:8000/categories/1" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Художественная литература",
    "description": "Обновленное описание: Романы, рассказы, повести, новеллы"
  }'
```

### 7. Частичное обновление категории
```bash
curl -X PUT "http://127.0.0.1:8000/categories/1" \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Только обновляем описание"
  }'
```

### 8. Удалить категорию
```bash
curl -X DELETE http://127.0.0.1:8000/categories/5
```

---

## Книги (Books)

### 1. Получить список всех книг
```bash
curl http://127.0.0.1:8000/books
```

### 2. Получить список книг с пагинацией
```bash
curl "http://127.0.0.1:8000/books?skip=0&limit=5"
```

### 3. Поиск книг по названию
```bash
curl "http://127.0.0.1:8000/books?title=Война"
```

### 4. Фильтрация книг по категории
```bash
curl "http://127.0.0.1:8000/books?category_id=1"
```

### 5. Комбинированная фильтрация (название + категория)
```bash
curl "http://127.0.0.1:8000/books?title=Python&category_id=3"
```

### 6. Получить книгу по ID
```bash
curl http://127.0.0.1:8000/books/1
```

### 7. Создать новую книгу
```bash
curl -X POST "http://127.0.0.1:8000/books" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Анна Каренина",
    "description": "Роман Льва Толстого о трагической любви",
    "price": 750.50,
    "url": "https://example.com/books/anna-karenina",
    "category_id": 1
  }'
```

### 8. Создать книгу без опциональных полей
```bash
curl -X POST "http://127.0.0.1:8000/books" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Новая книга",
    "category_id": 1
  }'
```

### 9. Обновить книгу полностью
```bash
curl -X PUT "http://127.0.0.1:8000/books/1" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Война и мир (обновленное издание)",
    "description": "Роман-эпопея Льва Толстого - полное издание",
    "price": 950.00,
    "url": "https://example.com/books/voina-i-mir-updated",
    "category_id": 1
  }'
```

### 10. Частичное обновление книги (только цена)
```bash
curl -X PUT "http://127.0.0.1:8000/books/1" \
  -H "Content-Type: application/json" \
  -d '{
    "price": 999.99
  }'
```

### 11. Изменить категорию книги
```bash
curl -X PUT "http://127.0.0.1:8000/books/1" \
  -H "Content-Type: application/json" \
  -d '{
    "category_id": 2
  }'
```

### 12. Удалить книгу
```bash
curl -X DELETE http://127.0.0.1:8000/books/1
```

---

## Примеры с обработкой ошибок

### Попытка создать категорию с существующим именем (ошибка 400)
```bash
curl -X POST "http://127.0.0.1:8000/categories" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Художественная литература",
    "description": "Дубликат"
  }'
```

### Получить несуществующую категорию (ошибка 404)
```bash
curl http://127.0.0.1:8000/categories/999
```

### Создать книгу с несуществующей категорией (ошибка 404)
```bash
curl -X POST "http://127.0.0.1:8000/books" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Тестовая книга",
    "category_id": 999
  }'
```

### Удалить категорию с книгами (ошибка 400)
```bash
curl -X DELETE http://127.0.0.1:8000/categories/1
```

---

## Примеры для Postman

### Настройки для Postman:
- **Method:** Выберите метод (GET, POST, PUT, DELETE)
- **URL:** `http://127.0.0.1:8000/categories` или `http://127.0.0.1:8000/books`
- **Headers:** 
  - `Content-Type: application/json` (для POST и PUT)
- **Body:** Выберите `raw` и `JSON`, затем вставьте JSON данные

### Пример JSON для создания книги:
```json
{
  "title": "Название книги",
  "description": "Описание книги",
  "price": 500.00,
  "url": "https://example.com/book",
  "category_id": 1
}
```

---

## Примеры для Python (requests)

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

# Получить все категории
response = requests.get(f"{BASE_URL}/categories")
print(response.json())

# Создать категорию
category_data = {
    "name": "Фантастика",
    "description": "Научная фантастика и фэнтези"
}
response = requests.post(f"{BASE_URL}/categories", json=category_data)
print(response.json())

# Получить книги с фильтрацией
response = requests.get(f"{BASE_URL}/books", params={"category_id": 1, "limit": 5})
print(response.json())

# Обновить книгу
book_data = {
    "price": 1200.00
}
response = requests.put(f"{BASE_URL}/books/1", json=book_data)
print(response.json())
```

---

## Полезные команды для тестирования

### Проверить все эндпоинты одной командой
```bash
echo "=== Health Check ===" && \
curl http://127.0.0.1:8000/health && \
echo -e "\n\n=== Все категории ===" && \
curl http://127.0.0.1:8000/categories && \
echo -e "\n\n=== Все книги ===" && \
curl http://127.0.0.1:8000/books
```

### Сохранить ответ в файл
```bash
curl http://127.0.0.1:8000/books > books_response.json
```

### Красивый вывод JSON (требует jq)
```bash
curl http://127.0.0.1:8000/books | jq
```
