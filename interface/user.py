from aiogram import types, Bot, Dispatcher, html
from aiogram.filters import CommandStart
import sqlite3
import asyncio
import logging
import sys
import os

import sqlalchemy.exc
from downloader import SocialMediaDownloader
from data import config
from data.database import DatabaseManager
from Filters import *
import yt_dlp
from yt_dlp import YoutubeDL
import sqlalchemy

db = DatabaseManager(db_url="postgresql://postgres:308012@localhost:5432/downloader_bot")
dp = Dispatcher()


@dp.message(CommandStart())
async def first(message:types.Message):
    try:
        await db.create_user(nickname=message.from_user.username, tg_id=message.from_user.id)
    except sqlalchemy.exc.IntegrityError:
        pass
    await message.answer(f'Привет {message.from_user.username}, это бот для скачивания видео из разных соц сетей, просто отправь ссылку')

@dp.message(UrlFilter())
async def download(message: types.Message):
    url = message.text
    platforms = ['youtube', 'instagram', 'facebook', 'vimeo', 'vkvideo']
    platform = next((p for p in platforms if p in url), None)

    if platform:
        try:
            await message.answer('Начинаю загрузку')

            # Используем yt_dlp для загрузки видео
            with YoutubeDL({'outtmpl': '%(title)s.%(ext)s'}) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                video_path = ydl.prepare_filename(info_dict)

            logging.info(f"Видео успешно загружено по пути: {video_path}")
            if os.path.exists(video_path):
                video_file = types.FSInputFile(video_path)
                await message.answer_video(video=video_file)
                os.remove(video_path)
            else: await message.answer('Файл не найден')
        except Exception as e:
            logging.error(f"Ошибка при отправке видео: {e}")
            await message.answer(f"Ошибка: {e}")
    else:
        await message.answer("Невозможно определить платформу для скачивания видео.")