import configparser
import datetime
import os
import cat_server_pb2
import cat_server_pb2_grpc
import grpc

from aiogram import Router, types
from aiogram.filters import Command
from filter import AdminFilter, ChatTypeFilter

default_router = Router()

last_message = None

user = int(os.environ['USER'])


@default_router.message(Command('start'))
async def start(message: types.Message):
    await message.reply("Привет! Я бот.")


@default_router.message(Command('help'))
async def start(message: types.Message):
    await message.answer('''Вот то, что я уже умею:
    /klabukow - Узнать, сколько времени @ klabukow не писал в чат
    
    /cat_fact - Узнать случайный факт про котов
    
    /help - Вывести все команды
    
    
    Бот написан и поддерживается @zakhaarovv.
    Ссылка на репозиторий бота: 
    https://github.com/arrowwhi/alexandr_time_bot
    ''')


@default_router.message(Command('klabukow'))
async def get_last_message_time(message: types.Message):
    if last_message:

        difference = datetime.datetime.now(datetime.timezone.utc) - last_message

        days, seconds = divmod(difference.total_seconds(), 24 * 3600)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        await message.reply(
            f"@klabukow не писал сообщение в чат {int(days)} дней {int(hours)} часов "
            f"{int(minutes)} минут {int(seconds)} секунд.")
    else:
        await message.reply("@klabukow еще не успел написать сообщение.")


@default_router.message(Command('cat_fact'))
async def get_cat_fact(message: types.Message):
    with grpc.insecure_channel('cat_fact:50051') as channel:
        stub = cat_server_pb2_grpc.CatFactServiceStub(channel)
        response = stub.GetResponse(cat_server_pb2.EmptyRequest())
        await message.answer(response.message)


@default_router.message(AdminFilter(time_user=user), ChatTypeFilter(chat_type=["group", "supergroup"]))
async def remember_last_message_time(message: types.Message):
    global last_message

    last_message = message.date
    # await message.reply("Я запомнил время вашего последнего сообщения.")
