from aiogram import Bot
from aiogram.types import BotCommand,BotCommandScopeDefault

async def set_commands(bot:Bot):
    comands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='help',
            description='Помощь'

        ),
        BotCommand(
            command='show_time',
            description='Показывает установленное время отправки сообщения'
        ),
        BotCommand(
            command='set_time',
            description='Устанавливает время отправки сообщения'
        ),
        BotCommand(
            command='delete_time',
            description='Удаляет время отправки сообщения'
        ),

    ]

    await bot.set_my_commands(comands, BotCommandScopeDefault())