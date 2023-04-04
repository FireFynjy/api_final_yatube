# api_final
Проект Yatube API Final

### Описание проекта:

Проект представляет собой реализацию API для социальной сети Yatube.

Позволяет получить доступ к постам, группам, комментариям и ленте подписок
через GET-запросы, а также их изменение через отправку POST, PUT, PATCH и DELETE запросов.

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