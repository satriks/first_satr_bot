from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from core.handlers.sched import cat_every_day
from core.utils.db_connect import Request
from core.utils.states_time import StateTime



async def del_times(message: Message, bot: Bot, request: Request):
    await request.del_time(message.from_user.id)
    await message.answer('Время удалено')

async def start_set_times(message: Message, state: FSMContext):
    await state.set_state(StateTime.GET_TIME)
    await message.answer('Введите когда прислать сообщение в формате час.минуты')

async def set_times(message: Message, bot: Bot, request: Request, state: FSMContext):

    await request.set_time(message.from_user.id, message.text)
    await message.answer('Время установлено')
    await state.clear()

async def show_time(message: Message, bot: Bot, request: Request):
    clock, = await request.get_user_time(message.from_user.id)
    if clock.get("time")  is not None:
        await message.answer(f'Сейчас установлено : {clock.get("time").strftime("%H:%M")} ')
    else:
        await message.answer(f'Время не установлено')