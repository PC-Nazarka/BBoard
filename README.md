# BBoard

## Реализованная функциональность
  - [x] регистрация пользователей;
  - [x] добавление / удаление / редактирования объявления;
  - [x] чат с другими пользователями;
  - [x] редактирование профиля пользователя;
  - [x] поиск объявлений.

## Зависимости
  - Python - основной язык программирования
  - Django - backend-часть приложения
  - Bootstrap - frontend-часть приложения
  - SQLite - основная база данных
  - redis - база данных для работы чата

## Окружение
1. Развёртывание производится на операционной системе Windows 10
2. Требуется предустановленный интерпретатор python версии 3.9.6
3. Необходимые к установке пакеты перечислены в pyproject.toml

## Развёртывание локально
Сперва необходимо развернуть у себя redis 5 с помощью Docker, либо скачав архив, распаковав который у вас будет
возможность запустить redis-cli и redis-server.

Запуск самого Django сервера производится в папке проекта при помощи следующей команды:
```bash
python manage.py runserver
```