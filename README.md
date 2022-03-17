# Темплейт с готовым Тротлингом и подключение к PostgreSQL с помощью библиотеки sqlalchemy.

## Технологии
* Python 3 - Язык на котором написан шаблон

* [aiogram](https://github.com/aiogram/aiogram) — работа с Telegram Bot API;
* [redis](https://redis.io) — персистентное хранение данных;
* [cachetools](https://cachetools.readthedocs.io/en/stable) — реализация троттлинга для борьбы с флудом (Сообщения\Нажатия);
* [sqlalchemy](https://www.sqlalchemy.org/docs/) - взаимодействие с базой данных PostgreSQL

## Найстройка

Создайте файл `bot.ini` в корне, предварительно скопировал туда содержимое из `bot.ini.example`,
подставьте свои данные. В разделе `throttling` указывайте нужную переменную и время в секундах,
после в `tgbot/config.py` добавьте их таким способом:

```python
        throttling = {
                # "default": TTLCache(maxsize=inf, ttl=int(throttling["default"])),
                # "main": TTLCache(maxsize=inf, ttl=int(throttling["main"])),
		":param key:": TTLCache(maxsize=inf, ttl=int(throttling["<name in bot.ini>"])), # То что мы добавили.
        }
```

## Благодарности

* [@Tishka17](https://t.me/Tishka17) за основу шаблона
* [@Groosha](https://t.me/Groosha) за помощь с обработкой

## Версия шаблона.

* SQLAlchemy version 0.0.1 
