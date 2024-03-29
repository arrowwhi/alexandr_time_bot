import asyncio
import os
# import configparser

import logging
from aiogram import Bot, Dispatcher
from router import default_router

global last_message


async def main():
    token = os.environ['TOKEN']
    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.INFO)
    # Объект бота
    bot = Bot(token=token)
    # Диспетчер
    dp = Dispatcher()

    dp.include_router(default_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
