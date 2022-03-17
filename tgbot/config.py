import configparser
from dataclasses import dataclass
from cachetools import TTLCache
from math import inf

@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str


@dataclass
class TgBot:
    token: str
    admin_id: int
    use_redis: bool
        
@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    throttling: dict


def cast_bool(value: str) -> bool:
    if not value:
        return False
    return value.lower() in ("true", "t", "1", "yes")


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)

    tg_bot = config["tg_bot"]
    throttling = config["throttling"]

    return Config(
        tg_bot=TgBot(
            token=tg_bot["token"],
            admin_id=int(tg_bot["admin_id"]),
            use_redis=cast_bool(tg_bot.get("use_redis")),
        ),
        db=DbConfig(**config["db"]),
        throttling = {
                "default": TTLCache(maxsize=inf, ttl=int(throttling["default"])), # bot.ini[throttling][default] of seconds
                "main": TTLCache(maxsize=inf, ttl=int(throttling["main"])), # bot.ini[throttling][main] of seconds
        }
    )
