from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.types import CallbackQuery

from tgbot.services.repository import Repo
from tgbot.middlewares.throttling import rate_limit


@rate_limit("default")
async def user_start(m: Message, repo: Repo):
    await repo.add_user(m.from_user.id, "+7...")
    await m.reply("Hello, user!")


@rate_limit("main")
async def throttling_call(call: CallbackQuery):
    await call.answer("You clicked on the button")


def register_user(dp: Dispatcher):
    # Message
    dp.register_message_handler(user_start, commands=["start"], state="*")
    # CallbackQuery
    dp.register_callback_query_handler(throttling_call, lambda c: c.data == "throttling", state="*")
    # or 
    # dp.register_callback_query_handler(throttling_call, lambda c: True, state="*")
