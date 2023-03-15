import asyncio

import requests
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Text, Command
import logging

from aiogram.types import URLInputFile
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler



from core.handlers.hendlers import send_weather2, send_cat, send_photo
from core.handlers.sched import send_every_day, cat_every_day
from core.keyboards.keyboard import main_keyboard
from core.midlware.database import DbSession
from core.utils.comands import set_commands
from settings import setting
from core.handlers.basic import get_start, process_help_command
from core.handlers.time_message import del_times, set_times, start_set_times, show_time
import asyncpg
from core.utils.db_connect import Request
from core.utils.states_time import StateTime
from core.handlers import time_message
from settings import database



async def start_bot(bot:Bot):
    await set_commands(bot)
    await bot.send_message(setting.bots.admin_id, text='Бот @firstsatrbot включился', reply_markup=main_keyboard())

async def stop_bot(bot:Bot):
    await bot.send_message(setting.bots.admin_id, text='Бот @firstsatrbot остановлен')

async def create_pool():
    credentials = {
        "user": 'postgres',
        "password": 'postgres',
        "database": 'user_tg',
        "host": "db",

    }
    return await asyncpg.create_pool(**credentials, port=5432,)


async def scheduler_job(pull, scheduler: AsyncIOScheduler, bot: Bot,):
    request = Request(pull)

    for i in await request.get_id():
        user_id, time = next(i.values())
        if time is None:
            continue
        scheduler.add_job(send_weather2, trigger='cron', hour=f'{time.hour}', minute=f'{time.minute}', args=(bot, user_id))


async def start():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - %(name)s -'
                               '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')


    bot = Bot(token=setting.bots.bot_token)
    poll_connect = await create_pool()

    dp = Dispatcher()
    dp.message.register(get_start, CommandStart())

    dp.update.middleware.register(DbSession(poll_connect))

    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')

    await scheduler_job(pull=poll_connect, scheduler=scheduler, bot=bot )

    dp.message.register(set_times, StateTime.GET_TIME)
    dp.message.register(del_times, Command('delete_time'))
    dp.message.register(start_set_times, Command('set_time'))
    dp.message.register(show_time, Command('show_time'))
    dp.message.register(process_help_command, Command('help'))
    dp.message.register(send_cat, Text(contains='кот', ignore_case=True))
    dp.message.register(send_cat, Text(contains='кош', ignore_case=True))
    dp.message.register(send_cat, Text(contains='кис', ignore_case=True))
    dp.message.register(send_weather2, Text(contains='погода', ignore_case=True))
    dp.message.register(send_photo)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    scheduler.start()
    try:
        await dp.start_polling(bot)
    except:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())