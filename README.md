# api_final

### Описание

Этот проект предназначается для авторов, которые хотят чтобы их посты, блоги увидел кто то другой, оценил и дал обратную связь, прокомментировав или лайкнув пост. Автором на нашем сайте будут доступны уникальные стили оформления их главной страницы, адрес и имя. Также они смогут сами модерировать комментарии, исправлять и редактировать посты даже после их публикации.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Grindelwaldoff/api_final_yatube.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3.7 -m venv venv
```

```
source venv/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

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

### Примеры запросов к API

Получение постов:

```
GET /api/v1/posts/

Content-Type application/json

{
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": 
[
        {}
    ]
}
```

Получение комментариев:

```
GET /api/v1/posts/{post_id}/comments/{id}/
Content-Type application/json

{
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
}
```

Список сообществ:

```
GET /api/v1/groups/
Content-Type application/json

[
    {
        "id": 0,
        "title": "string",
        "slug": "string",
        "description": "string"
    }
]
```

Подписка:

```
POST /api/v1/follow/
Content-Type application/json

Request:
    {
        "following": "string"
    }

Response:
    {
        "user": "string",
        "following": "string"
    }
```


### Разработчик:
Всеволод Рыбник tg: @Grindelwaldoff
