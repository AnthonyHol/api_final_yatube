# API для Yatube
## Спринт 9 — api_final_yatube

### Описание
API для проекта [Yatube](https://github.com/AnthonyHol/hw05_final "Yatube"). где реализованы следующие функции: публикация и изменение записей, их комментирование, а также механизм подписки на интересующих авторов.

### Технологии
- Python 3.7
- Django 2.2.19
- Django Rest Framework 3.12.4
- Djoser 2.0.1
- SimpleJWT 4.8.0

### Запуск проекта в dev-режиме
Клонируем проект:
```
git clone https://github.com/AnthonyHol/hw05_final.git
```

Переходим в папку с проектом и устанавливаем виртуальное окружение:
```
python -m venv venv
```

Активируем виртуальное окружение:
```
source venv/Scripts/activate
```

Устанавливаем зависимости:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

Выполняем миграции:
```
python yatube/manage.py makemigrations
```
```
python yatube/manage.py migrate
```

Создаем суперпользователя:
```
python yatube/manage.py createsuperuser
```

В папку, где находится файл settings.py, добавляем файл .env, куда прописываем секретный ключ следующим образом:
```
SECRET_KEY='Секретный ключ'
```

Запускаем проект:
```
python yatube/manage.py runserver
```

Проект будет доступен по адресу `http://127.0.0.1:8000/`

Переход на админ-панель доступен по адресу `http://127.0.0.1:8000/admin/`

### Пример работы с API

```
Для неавторизированных пользователей работа с API доступна лишь в режиме чтения:
GET api/v1/posts/ — получить список всех публикаций.
При указании параметров limit и offset выдача происходит с пагинацией
GET api/v1/posts/{id}/ — получение публикации по id

GET api/v1/groups/ — получение списка доступных сообществ
GET api/v1/groups/{id}/ — получение информации о сообществе по id

GET api/v1/{post_id}/comments/ — получение всех комментариев к публикации
GET api/v1/{post_id}/comments/{id}/ — Получение комментария к публикации по id
```
Для авторизированных пользователей также доступны запросы на создание, изменение и удаление.

Подробная документация по всем URL и запросам предоставлена по адресу `http://127.0.0.1:8000/redoc/`.


Автор: [Холкин Антон](https://github.com/AnthonyHol/ "Холкин Антон")
