from aiogram.fsm.storage import memory
from aiogram import Bot, Dispatcher, types

from data import config

bot = Bot(token=config.get_token())
dp = Dispatcher(bot)

