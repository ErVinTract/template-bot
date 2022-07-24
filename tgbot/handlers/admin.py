from aiogram import Dispatcher, types

from tgbot.models.role import UserRole


async def admin_start(m: types.Message):
    await m.reply("Hello, admin! :)")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(
        admin_start, commands=["start"], state="*", role=UserRole.ADMIN,
    )
    # Either you can pass multiple roles:
    # dp.register_message_handler(
    #     admin_start, commands=["start"], state="*", role=[UserRole.ADMIN],
    # )
    # Or use another filter:
    # dp.register_message_handler(
    #     admin_start, commands=["start"], state="*", is_admin=True,
    # )
