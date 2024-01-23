import asyncio
import configparser

import logging
from aiogram import Bot, Dispatcher
from router import default_router

global last_message


async def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    token = config.get('Telegram', 'token')
    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.INFO)
    # Объект бота
    bot = Bot(token=token)
    # Диспетчер
    dp = Dispatcher()

    dp.include_router(default_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
