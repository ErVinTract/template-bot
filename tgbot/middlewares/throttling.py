from aiogram import types
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware


def rate_limit(key="default"):
    """
    Decorator for applying trottling to the handler
    :param key: id of a specific trottling

    """

    def decorator(func):
        setattr(func, 'throttling_key', key)
        return func
    return decorator


class ThrottlingMiddleware(BaseMiddleware):
    """
    Middleware for "smart" trottling
    """

    def __init__(self, caches: dict):
        super(ThrottlingMiddleware, self).__init__()
        self.caches = caches

    async def on_process_message(self, message: types.Message, data: dict):
        """
        This handler will work when processing a message (message class)
        :param message: incoming Telegram message
        """
        # Getting the current handler
        handler = current_handler.get()

        # We determine which cache should be used
        throttling_key = getattr(handler, 'throttling_key', None)

        # If such a cache is available, then add from_id
        # to the temporary list and perform trolling or skip it altogether
        if throttling_key and throttling_key in self.caches:
            if not self.caches[throttling_key].get(message.from_user.id):
                self.caches[throttling_key][message.from_user.id] = True
                return
            else:
                raise CancelHandler

    async def on_process_callback_query(self, call: types.CallbackQuery, data: dict):
        """
        This handler will work when processing the inline button (CallbackQuery class)
        :param message: incoming Telegram message
        """

        # Getting the current handler
        handler = current_handler.get()

        # We determine which cache should be used
        throttling_key = getattr(handler, 'throttling_key', None)

        i18n = data['i18n']

        # If such a cache is available, then add from_id
        # to the temporary list and perform trolling or skip it altogether
        if throttling_key and throttling_key in self.caches:
            if not self.caches[throttling_key].get(call.from_user.id):
                self.caches[throttling_key][call.from_user.id] = True
                return
            else:
                await call.answer(i18n.throttling.exception.text())
                raise CancelHandler
