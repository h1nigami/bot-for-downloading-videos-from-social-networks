from aiogram.filters import Filter
from aiogram import types

class UrlFilter(Filter):
    async def __call__(self, message: types.Message) -> bool:
        return ("https://" in message.text or "http://" in message.text) and any(
            platform in message.text for platform in ["youtube", "instagram", "facebook", "vimeo", "vkvideo"]
        )