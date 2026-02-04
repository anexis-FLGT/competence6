#!/usr/bin/env python3
"""
Скрипт для проверки подключения к базе данных
"""
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

database_url = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/books_db")

print(f"Попытка подключения к: {database_url.split('@')[1] if '@' in database_url else 'не указано'}")

try:
    engine = create_engine(database_url)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        version = result.fetchone()[0]
        print("✅ Подключение к PostgreSQL успешно!")
        print(f"Версия PostgreSQL: {version.split(',')[0]}")
        
        # Проверка существования таблиц
        result = conn.execute(text("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """))
        tables = [row[0] for row in result]
        if tables:
            print(f"\nТаблицы в базе данных: {', '.join(tables)}")
        else:
            print("\n⚠️  Таблицы еще не созданы. Они будут созданы при первом запуске приложения.")
            
except Exception as e:
    print(f"❌ Ошибка подключения: {e}")
    print("\nПроверьте настройки в файле .env:")
    print("DATABASE_URL=postgresql://username:password@localhost:5432/books_db")
    print("\nДля пользователя 'octagon' команда может быть:")
    print("DATABASE_URL=postgresql://octagon:your_password@localhost:5432/books_db")

