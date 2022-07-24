from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from tgbot.services.repository import Repo
from tgbot.markups.user import UserMarkup, FormCallback
from tgbot.states.user import UserState
from tgbot.middlewares.throttling import rate_limit

from aiogram.utils.callback_data import CallbackData
from fluentogram import TranslatorRunner, TranslatorHub


@rate_limit()  # throttling key = 'default'
async def user_start(m: types.Message, repo: Repo, i18n: TranslatorRunner, state: FSMContext):
    await repo.add_user(userid=m.from_user.id)
    markup = UserMarkup.get_start_keyboard(i18n)

    text = i18n.welcome.text(user=m.from_user.full_name)
    await m.answer(text=text, reply_markup=markup)
    await state.set_state(UserState.CHANGE_LANG)


@rate_limit("main")
async def cb_change_lang(call: types.CallbackQuery, i18n: TranslatorRunner):
    markup = UserMarkup.get_select_language()

    text = i18n.change.lang.menu()
    await call.message.edit_text(text=text, reply_markup=markup)


@rate_limit("main")
async def change_lang(call: types.CallbackQuery,
                      repo: Repo,
                      callback_data: CallbackData,
                      i18n_hub: TranslatorHub,
                      state: FSMContext):
    lang_code = callback_data['lang_code']
    i18n = i18n_hub.get_translator_by_locale(lang_code)

    await call.answer(i18n.change.lang.success())
    await repo.change_user_lang(call.from_user.id, lang_code)

    await call.message.delete()
    await state.finish()


def register_user(dp: Dispatcher):
    # Message
    dp.register_message_handler(user_start, commands=["start"], state="*")

    # CallbackQuery
    dp.register_callback_query_handler(
        cb_change_lang,
        text="change_lang",
        state=UserState.CHANGE_LANG
    )
    dp.register_callback_query_handler(
        change_lang,
        FormCallback.change_lang.filter(),
        state=UserState.CHANGE_LANG
    )
