import configparser
from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message


class AdminFilter(BaseFilter):
    def __init__(self, time_user: int):
        self.admin_list = time_user

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == self.admin_list
