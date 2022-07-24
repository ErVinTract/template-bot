from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from fluentogram import TranslatorRunner


class FormCallback:
    change_lang = CallbackData('lang', "lang_code")


class UserMarkup:
    def get_start_keyboard(i18n: TranslatorRunner) -> InlineKeyboardMarkup:
        keyboard = [
            [
                InlineKeyboardButton(
                    text=i18n.change.lang.btn(), callback_data="change_lang"
                )
            ]
        ]
        return InlineKeyboardMarkup(inline_keyboard=keyboard)

    def get_select_language() -> InlineKeyboardMarkup:
        keyboard = [
            [
                InlineKeyboardButton(
                    text="🇺🇸", callback_data=FormCallback.change_lang.new(lang_code='en')
                ),
                InlineKeyboardButton(
                    text="🇷🇺", callback_data=FormCallback.change_lang.new(lang_code='ru')
                ),
            ]
        ]
        return InlineKeyboardMarkup(inline_keyboard=keyboard)
