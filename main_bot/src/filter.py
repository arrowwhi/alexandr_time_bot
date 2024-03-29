
from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message


class AdminFilter(BaseFilter):
    def __init__(self, time_user: int):
        self.admin_list = time_user

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == self.admin_list


class ChatTypeFilter(BaseFilter):  # [1]
    def __init__(self, chat_type: Union[str, list]): # [2]
        self.chat_type = chat_type

    async def __call__(self, message: Message) -> bool:  # [3]
        if isinstance(self.chat_type, str):
            return message.chat.type == self.chat_type
        else:
            return message.chat.type in self.chat_type


class YesFilter(BaseFilter):
    def __call__(self, message: Message):
        return message.text.lower().endswith('да')
