# Описание приложения

Запуск проекта.
 - Скопировать проект с помощью ``` git clone https://github.com/iNgredie/Parser-HackerNews.git ```
 - В корневой папке через терминал запустить докер командой
 - ```docker-compose up --build ```  собрать приложение и сделать его первоначальный запуск
 - ```docker-compose down -v``` – остановить работу приложения
 - ```docker-compose run web python manage.py migrate``` – сделать необходимые миграции
 - ```docker-compose up``` – окончательно запустить приложение.


Стек технологий и требований к ним для реализации веб-приложения 

- Python 3
- Django 
- СУБД PostgreSQL (через отдельный Docker-образ)
- Контейнер с приложением должен использовать alpine

Задача:  
Нужно создать приложение агрегатор новостей Hacker News.   
Hacker News - https://news.ycombinator.com


Техническое описание  
Необходимо создать приложение, которое будет периодически парсить главную страницу Hacker News, вытягивая из нее список постов
и сохраняя в базу данных.   
А еще приложение должно иметь HTTP API с всего одним методом (GET /posts), с помощью которого можно будет получить список всех
доступных (собранных) новостей.   
По каждой новости необходимо иметь заголовок и URL, а также время, когда она была сохранена в БД. Достаточно сохранять только 30
новостей и приходить за новыми через определенный интервал времени, либо по-требованию.

- API метод для получения списка новостей на запрос:    
    ``` http://localhost:8000/posts/```

- Результат список новостей в формате JSON:   
```[
 {"id": 1, "title": "Announcing Rust 1.33.0", "url": "https://example.
com", "created": "ISO 8601"},
 {"id": 2, "title": "Redesigning GitHub Repository Page", "url":
"https://example.com", "created": "ISO 8601"}
]
```
- Есть сортировка по заданному атрибуту, по возрастанию и убыванию.   
    ``` http://localhost:8000/posts?order=title```

- Так же клиент имеет возможность запросить подмножество данных, указав offset и limit. Пусть по-умолчанию API возвращает 5
постов.   
```http://localhost:8000/posts/?offset=10&limit=10```   

- Парсер новостей с сайта Hacker News - https://news.ycombinator.com запускается командой:   
```docker-compose run web python manage.py added_news```