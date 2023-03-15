import aiohttp
from aiogram import Bot
from aiogram.types import Message, URLInputFile

from core.YandexWeatherAPI.api_weather import get_weather
from core.keyboards.keyboard import main_keyboard



async def send_weather2(message: Message, bot: Bot):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://aws.random.cat/meow') as response:
            cat = await response.json()
            text, = await get_weather()
            cat_response = cat['file']
            await message.answer(text=text)
            await message.answer_photo(URLInputFile(cat_response), caption='Котик для настроения', reply_markup=main_keyboard())


async def send_cat(message: Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://aws.random.cat/meow') as response:
            cat = await response.json()
            cat_response = cat['file']
            await message.answer_photo(URLInputFile(cat_response), caption='Котик для настроения', reply_markup=main_keyboard())

async def send_photo(message: Message):
    await message.answer_photo(URLInputFile('https://picsum.photos/1200/800'), caption='Случайное фото', reply_markup=main_keyboard())




