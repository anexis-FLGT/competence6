-- SQL запросы для проверки данных в базе данных
-- Выполните эти запросы в psql и сделайте скриншот результатов

-- Подключение к базе данных (выполните в терминале):
-- Вариант 1 (через TCP/IP, рекомендуется для WSL):
-- psql -h localhost -U octagon -d books_db
-- 
-- Вариант 2 (если нужен пароль):
-- export PGPASSWORD=your_password
-- psql -h localhost -U octagon -d books_db
--
-- Вариант 3 (через пользователя postgres):
-- psql -h localhost -U postgres -d books_db

-- 1. Просмотр всех категорий
SELECT * FROM categories;

-- 2. Просмотр всех книг
SELECT * FROM books;

-- 3. Просмотр книг с названиями категорий (JOIN)
SELECT 
    b.id,
    b.title,
    b.description,
    b.price,
    b.url,
    c.name AS category_name,
    c.description AS category_description
FROM books b
JOIN categories c ON b.category_id = c.id
ORDER BY b.id;

-- 4. Количество книг в каждой категории
SELECT 
    c.id,
    c.name,
    COUNT(b.id) AS books_count
FROM categories c
LEFT JOIN books b ON c.id = b.category_id
GROUP BY c.id, c.name
ORDER BY c.id;

-- 5. Структура таблицы categories
\d categories

-- 6. Структура таблицы books
\d books
