from aiogram import types, Bot, Dispatcher, html
from aiogram.filters import CommandStart
import asyncio
import logging
import sys

from data import config, db


dp = Dispatcher()

async def main():
    bot = Bot(token=config.get_token('BOT', 'token'), parse_mode=types.ParseMode.HTML)
    await dp.start_polling(bot)

@dp.message(CommandStart())
async def first(message:types.Message):
    await db.create_user(nickname=message.from_user.username, tg_id=message.from_user.id)
    await message.answer(f'Привет {message.from_user.username}, это бот для скачивания видео из разных соц сетей, просто отправь ссылку')

