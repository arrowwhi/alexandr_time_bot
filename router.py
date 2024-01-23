import configparser
import datetime

from aiogram import Router, types
from aiogram.filters import Command
from filter import AdminFilter, ChatTypeFilter


default_router = Router()

last_message = None

config = configparser.ConfigParser()
config.read('config.ini')
user = int(config.get('Telegram', 'user'))
print(user)


@default_router.message(Command('start'))
async def start(message: types.Message):
    await message.reply("Привет! Я бот.")


@default_router.message(Command('last'))
async def get_last_message_time(message: types.Message):
    if last_message:

        difference = datetime.datetime.now(datetime.timezone.utc) - last_message

        days, seconds = divmod(difference.total_seconds(), 24 * 3600)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        await message.reply(f"@klabukow не писал сообщение в чат {int(days)} дней {int(hours)} часов {int(minutes)} минут {int(seconds)} секунд.")
    else:
        await message.reply("Вы еще не отправляли сообщений.")


@default_router.message(AdminFilter(time_user=user), ChatTypeFilter(chat_type=["group", "supergroup"]))
async def remember_last_message_time(message: types.Message):
    global last_message

    last_message = message.date
    await message.reply("Я запомнил время вашего последнего сообщения.")
