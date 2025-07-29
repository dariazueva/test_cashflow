# test_cashflow
Django CashFLow Service

## Описание

Веб-сервис для управления  движением денежных средств (ДДС), реализованный на Python, Django, PostgreSQL с использованием стандратной Django Admin и Django Rest Framework для API.

## Требования

- Python 3.12
- PostgreSQL
- Django
- Django Rest Framework

### Возможности
- CRUD-операции для учёта денежных операций
- Поддержка статусов, типов операций, категорий и подкатегорий
- Логические зависимости:
  - Категории привязаны к типам операций
  - Подкатегории привязаны к категориям
- Автоматическая валидация связей при создании записей
- Просмотр, фильтрация и управление записями через Django Admin
- REST API для интеграции с внешними сервисами

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:dariazueva/test_cashflow.git
```
```
cd cashflow
```
Cоздать и активировать виртуальное окружение:
```
python -m venv env
```
* Если у вас Linux/macOS
    ```
    source env/bin/activate
    ```
* Если у вас windows
    ```
    source env/Scripts/activate
    ```
```
python -m pip install --upgrade pip
```
Установите необходимые зависимости:
```bash
pip install -r requirements.txt
```
Создайте файл .env и заполните его своими данными по образцу:
```
POSTGRES_DB=cashflow_db
POSTGRES_USER=cashflow_user
POSTGRES_PASSWORD=mysecretpassword
DB_HOST=localhost
DB_PORT=5432
```
#### Выполнить миграции:
```bash
python manage.py migrate
```
#### Создайте суперюзера для доступа к админке:
```bash
python manage.py createsuperuser
```
#### Запустить проект:
```bash
python manage.py runserver
```
#### Запуcтите тесты:
```bash
python manage.py test
```
#### Интерфейс
- Основное управление — через Django Admin (/admin/)
- Все операции (создание, редактирование, удаление, фильтрация) доступны в админке
- REST API можно использовать для внешних интеграций или расширения фронтенда

## Автор
Зуева Дарья Дмитриевна
Github https://github.com/dariazueva/