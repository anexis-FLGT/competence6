# Инструкция по развертыванию на GitHub

## Подготовка проекта

1. Убедитесь, что все файлы созданы и проект работает локально
2. Проверьте, что папка `examples/` содержит скриншоты работы API
3. Убедитесь, что `.env` файл добавлен в `.gitignore` (не должен попасть в репозиторий)

## Создание репозитория на GitHub

1. Создайте новый публичный репозиторий на GitHub
2. Назовите его, например: `books-api-fastapi` или `competence6`

## Инициализация Git и загрузка кода

```bash
# Инициализация Git репозитория
git init

# Добавление всех файлов
git add .

# Создание первого коммита
git commit -m "Initial commit: FastAPI Books API with CRUD operations"

# Добавление удаленного репозитория (замените URL на ваш)
git remote add origin https://github.com/your-username/your-repo-name.git

# Отправка кода на GitHub
git branch -M main
git push -u origin main
```

## Структура коммитов (рекомендуется)

Можно разбить на несколько коммитов:

```bash
# 1. Базовая структура проекта
git add requirements.txt .gitignore README.md
git commit -m "Add project structure and dependencies"

# 2. Модели и схемы
git add app/models.py app/schemas.py app/database.py
git commit -m "Add database models and Pydantic schemas"

# 3. Роутеры
git add app/routers/
git commit -m "Add CRUD routers for categories and books"

# 4. Main приложение
git add main.py run.py
git commit -m "Add main application with health check endpoint"

# 5. Документация и примеры
git add examples/ TESTING.md DEPLOYMENT.md
git commit -m "Add documentation and examples"

# Отправка всех коммитов
git push -u origin main
```

## Проверка

После загрузки проверьте:

1. ✅ Репозиторий публичный
2. ✅ Все файлы загружены
3. ✅ README.md отображается корректно
4. ✅ Папка examples/ содержит скриншоты
5. ✅ .env файл НЕ попал в репозиторий (проверьте через веб-интерфейс GitHub)

## Дополнительные файлы (опционально)

Можно добавить:

- `.github/workflows/` - для CI/CD
- `docker-compose.yml` - для упрощения развертывания
- `Dockerfile` - для контейнеризации приложения

## Ссылка на репозиторий

После завершения отправьте ссылку на репозиторий в формате:
```
https://github.com/your-username/your-repo-name
```

