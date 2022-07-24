from typing import Any

from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from fluentogram import TranslatorRunner

from tgbot.services.repository import Repo
from tgbot.services.fluent import FluentService


class LangMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self, fluent: FluentService):
        super().__init__()
        self.fluent = fluent

    async def pre_process(self, obj, data, *args) -> Any:

        fluent: FluentService = self.fluent
        repo: Repo = data["repo"]

        user = await repo.get_user(userid=obj.from_user.id)

        user_lang = user.get("lang") if user else 'en'
        translator_runner: TranslatorRunner = fluent.get_translator_by_locale(
            user_lang)
        data["i18n"] = translator_runner
        data["i18n_hub"] = fluent.hub
