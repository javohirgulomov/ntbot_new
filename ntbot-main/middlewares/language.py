import gettext
import os
from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from utils.queries.users import get_user


class PyBabelMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:

        user_lang = "en"

        if hasattr(event, 'from_user') and event.from_user:
            user = await get_user(chat_id=event.from_user.id)

            if user and user.get('language'):
                user_lang = user.get('language')
            elif event.from_user.language_code:
                user_lang = event.from_user.language_code.split('-')[0]

        root_dir = os.getcwd()
        locales_dir = os.path.join(root_dir, 'locales')

        try:
            translation = gettext.translation(
                domain='messages',
                localedir=locales_dir,
                languages=[user_lang]
            )
            data["_"] = translation.gettext
        except Exception as e:
            data["_"] = lambda s, locale=None: s

        return await handler(event, data)


def setup_middleware(dp):
    middleware = PyBabelMiddleware()
    dp.message.outer_middleware(middleware)
    dp.callback_query.outer_middleware(middleware)