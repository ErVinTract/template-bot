# �������� � ������� ���������� � ����������� � PostgreSQL � ������� ���������� asyncpg.

## ����������
* Python 3 - ���� �� ������� ������� ������

* [aiogram](https://github.com/aiogram/aiogram) � ������ � Telegram Bot API;
* [redis](https://redis.io) � ������������� �������� ������;
* [cachetools](https://cachetools.readthedocs.io/en/stable) � ���������� ���������� ��� ������ � ������ (���������\�������);
* [asyncpg](https://magicstack.github.io/asyncpg/current/) - �������������� � ����� ������ PostgreSQL

## ����������

�������� ���� `bot.ini` � �����, �������������� ���������� ���� ���������� �� `bot.ini.example`,
���������� ���� ������. � ������� `throttling` ���������� ������ ���������� � ����� � ��������,
����� � `tgbot/config.py` �������� �� ����� ��������:

```python
        throttling = {
                # "default": TTLCache(maxsize=inf, ttl=int(throttling["default"])),
                # "main": TTLCache(maxsize=inf, ttl=int(throttling["main"])),
		":param key:": TTLCache(maxsize=inf, ttl=int(throttling["<name in bot.ini>"])), # �� ��� �� ��������.
        }
```

## �������������

* [@Tishka17](https://t.me/Tishka17) �� ������ �������
* [@Groosha](https://t.me/Groosha) �� ������ � ����������

## ������ �������.

* 0.0.1