from interface import dp
from aiogram import Bot
import logging
import sys
import asyncio
from data import config

bot = Bot(token=config.get_token())

async def start():
    await dp.start_polling(bot)
    print('Бот запущен')
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

if __name__ == '__main__':
   asyncio.run(start())