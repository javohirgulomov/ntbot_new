import logging
from aiogram import types
from core.db_settings import execute_query

logger = logging.getLogger(__name__)

async def get_user(chat_id: int) -> dict | None:
    """
    Get user from database by chat_id
    """
    try:
        query = "SELECT * FROM users WHERE chat_id = %s"
        params = (chat_id,)
        user = execute_query(query=query, params=params, fetch="one")
        return user
    except Exception as e:
        logger.error(msg=e)
        return None

async def add_user(data: dict) -> bool | None:
    """
    Create initial user with language, chat_id, and username only
    (Called when user selects language)
    """
    try:
        query = ("INSERT INTO users (chat_id, username, language) "
                 "VALUES (%s, %s, %s)")
        params = (data.get('chat_id'), data.get('username'), data.get('language'))
        return execute_query(query=query, params=params)
    except Exception as e:
        logger.error(msg=e)
        return None

async def update_user(data: dict, message: types.Message) -> bool | None:
    """
    Update user with complete registration info
    (Called after user completes all registration steps)
    """
    try:
        query = ("UPDATE users SET full_name = %s, phone_number = %s, "
                 "longitude = %s, latitude = %s WHERE chat_id = %s")
        params = (data.get('full_name'), data.get('phone_number'),
                  data.get('longitude'), data.get('latitude'),
                  message.from_user.id)
        return execute_query(query=query, params=params)
    except Exception as e:
        logger.error(msg=e)
        return None