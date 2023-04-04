# api_final
Проект Yatube API Final

### Описание проекта:

Проект представляет собой реализацию API для социальной сети Yatube.

Позволяет получить доступ к постам, группам, комментариям и ленте подписок
через GET-запросы, а также их изменение через отправку POST, PUT, PATCH и DELETE запросов.

### Автор проекта:

Антон Лопатин, Python-разработчик

### Стэк, используемый в проекте:

Python 3.11
Django 3.2.16
Django Rest Framework 3.12.4
Simple JWT 4.7.2
Djoser 2.1.0
Pillow 9.3.0.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:FireFynjy/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов к API:

Получить список всех постов

```
api/v1/posts
```

Получить пост по id

```
api/v1/posts/1
```

Получить список всех комментариев к определенному посту

```
api/v1/posts/1/comments
```

Получить текст комментария к определенному посту

```
api/v1/posts/1/comments/1
```

Получить список всех групп

```
api/v1/groups
```

Получить список всех подписок

```
api/v1/follow
```

### Примеры ответов от эндпоинтов:

GET-запрос к api/v1/posts

```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

POST-запрос к api/v1/posts

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

GET, PUT, PATCH-запрос к api/v1/posts/1

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

GET-запрос к api/v1/posts/1/comments

```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```

POST-запрос к api/v1/posts/1/comments/

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

GET, PUT, PATCH-запрос к api/v1/posts/1/comments/1

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

GET-запрос к api/v1/groups

```
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```

GET-запрос к api/v1/follow

```
[
  {
    "user": "string",
    "following": "string"
  }
]
```

POST-запрос к api/v1/follow

```
{
  "refresh": "string",
  "access": "string"
}
```