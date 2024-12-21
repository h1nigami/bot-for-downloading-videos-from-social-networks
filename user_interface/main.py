from aiogram import types, Bot, Dispatcher, html
import logging
import sys
from ..data.config import Config

config = Config('config.ini')

dp = Dispatcher()

async def main():
    bot = Bot(token=config.get_token('BOT', 'token'), parse_mode=types.ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)