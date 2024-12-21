from aiogram import types, Bot, Dispatcher, html
from aiogram.filters import CommandStart
import sqlite3
import asyncio
import logging
import sys
import os
from downloader import SocialMediaDownloader
from data import config, db
from Filters import *
import yt_dlp

dp = Dispatcher()

async def main():
    bot = Bot(token=config.get_token('BOT', 'token'), parse_mode=types.ParseMode.HTML)
    await dp.start_polling(bot)

class VideoFile(types.InputFile):
    def read(self, offset: int) -> bytes:
        return b''


@dp.message(CommandStart())
async def first(message:types.Message):
    try:
        await db.create_user(nickname=message.from_user.username, tg_id=message.from_user.id)
    except sqlite3.IntegrityError:
        pass
    await message.answer(f'Привет {message.from_user.username}, это бот для скачивания видео из разных соц сетей, просто отправь ссылку')

@dp.message(UrlFilter())
async def download(message: types.Message):
    url = message.text
    platforms = ['youtube', 'instagram', 'facebook', 'vimeo', 'vkvideo']
    platform = next((p for p in platforms if p in url), None)
    if platform:
        downloader = SocialMediaDownloader(url=url)
        try:
            #TODO
            #Исправить ошибку: Не видит файл
            await message.answer('Начинаю загрузку')
            downloader.download_with_retry(platform=platform)
            info_dict = yt_dlp.YoutubeDL.extract_info(url=url, download=False)
            video_path = f"{yt_dlp.YoutubeDL.prepare_filename(info_dict=info_dict)}"
            video_file = VideoFile(filename=video_path)
            await message.answer_video(video_file)
        except Exception as e:
            await message.answer(f"Ошибка: {e}")
    else:
        await message.answer("Невозможно определить платформу для скачивания видео.")