import asyncio
import logging

from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tgbot.config import load_config
from tgbot.filters.role import RoleFilter, AdminFilter
from tgbot.handlers.admin import register_admin
from tgbot.handlers.user import register_user
from tgbot.middlewares.db import DbMiddleware
from tgbot.middlewares.role import RoleMiddleware
from tgbot.middlewares.lang import LangMiddleware
from tgbot.middlewares.throttling import ThrottlingMiddleware
from tgbot.services.fluent import FluentService, TranslationLoader

import asyncpg

logger = logging.getLogger(__name__)


def _configure_fluent():
    locales_map = {
        "ru": ("ru", "en"),
        "en": ("en", "ru"),
    }
    loader = TranslationLoader(
        Path("tgbot/services/locales/"),
    )
    return FluentService(loader, locales_map)


async def create_pool(user, password, database, host):
    pool = await asyncpg.create_pool(
        host=host,
        user=user,
        password=password,
        database=database,
    )
    return pool


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")
    config = load_config("bot.ini")

    if config.tg_bot.use_redis:
        storage = RedisStorage2()
    else:
        storage = MemoryStorage()

    pool = await create_pool(
        user=config.db.user,
        password=config.db.password,
        database=config.db.database,
        host=config.db.host,
    )

    fluent = _configure_fluent()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher(bot, storage=storage)
    dp.middleware.setup(ThrottlingMiddleware(config.throttling))
    dp.middleware.setup(DbMiddleware(pool))
    dp.middleware.setup(RoleMiddleware(config.tg_bot.admin_id))
    dp.middleware.setup(LangMiddleware(fluent=fluent))

    dp.filters_factory.bind(RoleFilter)
    dp.filters_factory.bind(AdminFilter)

    register_admin(dp)
    register_user(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
