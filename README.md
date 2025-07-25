# Django Dynamic Form

## Описание
Форма с динамическим добавлением инпутов через jQuery. Данные сохраняются в PostgreSQL (JSONB).

## Развертывание проекта:
1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/ElizavetaDulub/qazx11.git
   cd django_dynamic_form
   
2. Создать и активировать виртуальное окружение:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   
3. Установить зависимости:
   ```bash
   pip install -r requirements.txt

4. Настроить PostgreSQL:
   База данных: forms_data

5. Выполнить миграции:
   ```bash
   python manage.py migrate

6. Запустить сервер:
   ```bash
   python manage.py runserver

7. Открыть в браузере:
   Форма ввода: http://127.0.0.1:8000/
   Список: http://127.0.0.1:8000/members/
