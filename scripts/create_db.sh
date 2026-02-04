#!/bin/bash
# Скрипт для создания базы данных books_db

echo "Создание базы данных books_db..."

# Попытка создать базу данных
# Замените 'postgres' на ваше имя пользователя PostgreSQL, если отличается
psql -U postgres -c "CREATE DATABASE books_db;" 2>/dev/null

if [ $? -eq 0 ]; then
    echo "База данных books_db успешно создана!"
else
    echo "Ошибка при создании базы данных."
    echo "Попробуйте выполнить вручную:"
    echo "  sudo -u postgres psql -c 'CREATE DATABASE books_db;'"
    echo "или"
    echo "  psql -U postgres -c 'CREATE DATABASE books_db;'"
    echo ""
    echo "Если база данных уже существует, это нормально."
fi

