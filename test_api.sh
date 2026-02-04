#!/bin/bash
# Скрипт для тестирования API

BASE_URL="http://127.0.0.1:8000"

echo "=== 1. Health Check ==="
curl -s "$BASE_URL/health" | python3 -m json.tool
echo -e "\n"

echo "=== 2. Получить все категории ==="
curl -s "$BASE_URL/categories" | python3 -m json.tool
echo -e "\n"

echo "=== 3. Получить все книги ==="
curl -s "$BASE_URL/books" | python3 -m json.tool
echo -e "\n"

echo "=== 4. Получить категорию по ID (ID=1) ==="
curl -s "$BASE_URL/categories/1" | python3 -m json.tool
echo -e "\n"

echo "=== 5. Получить книгу по ID (ID=1) ==="
curl -s "$BASE_URL/books/1" | python3 -m json.tool
echo -e "\n"

echo "=== 6. Фильтрация книг по категории (category_id=1) ==="
curl -s "$BASE_URL/books?category_id=1" | python3 -m json.tool
echo -e "\n"

echo "=== 7. Поиск книг по названию (title=Python) ==="
curl -s "$BASE_URL/books?title=Python" | python3 -m json.tool
echo -e "\n"

echo "=== 8. Поиск категорий по имени (name=Художественная) ==="
curl -s "$BASE_URL/categories?name=Художественная" | python3 -m json.tool
echo -e "\n"

echo "=== Тестирование завершено ==="
