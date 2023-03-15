from io import BytesIO

import aiohttp
import requests
from aiogram import Bot
from aiogram.types import URLInputFile, InputFile, BufferedInputFile

from core.YandexWeatherAPI.api_weather import get_weather
from settings import setting


async def send_every_day(bot: Bot):
    text, pict = get_weather()
    await bot.send_message(setting.bots.admin_id, text=text)

async def cat_every_day(bot:Bot, user_id: int ):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://aws.random.cat/meow') as response:
            cat = await response.json()
            async with session.get(cat['file']) as response2:
                cat_photo_data = await response2.content.read()
                cat_photo = BufferedInputFile(cat_photo_data, filename='cat_photo')
                await bot.send_photo(chat_id=user_id, photo=cat_photo, caption='Котик для настроения')