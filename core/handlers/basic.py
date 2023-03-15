from aiogram import Bot
from aiogram.types import Message


from core.utils.db_connect import Request


async def get_start(message: Message, bot: Bot, request: Request):
    await request.add_data(message.from_user.id, message.from_user.full_name, message.from_user.username)
    # await add_offer(message)
    await bot.send_message(message.from_user.id, f'Привет')
    print(f'Добавил к БД {message.from_user.id}')

async def process_help_command(message: Message, bot: Bot):
    await message.answer('Помощь, потом заполню')

# async def del_times(message: Message, bot: Bot, request: Request):
#     await request.del_time(message.from_user.id)
#     await message.answer('Время удалено')
#
# async def set_times(message: Message, bot: Bot, request: Request):
#     await request.set_time(message.from_user.id, message.text)
#     await message.answer('Время установлено')