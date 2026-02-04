#!/bin/bash
# Скрипт для выполнения SELECT запросов в PostgreSQL и создания скриншота

# Попробуйте один из вариантов подключения:

# Вариант 1: Через localhost (TCP/IP)
echo "Попытка подключения через localhost..."
psql -h localhost -U octagon -d books_db -f psql_select_queries.sql

# Если не работает, попробуйте вариант 2:
# psql -h 127.0.0.1 -U octagon -d books_db -f psql_select_queries.sql

# Если не работает, попробуйте вариант 3 (с паролем через переменную окружения):
# export PGPASSWORD=your_password
# psql -h localhost -U octagon -d books_db -f psql_select_queries.sql

# Если не работает, попробуйте вариант 4 (подключение через пользователя postgres):
# psql -h localhost -U postgres -d books_db -f psql_select_queries.sql
