from environs import Env
from dataclasses import dataclass

@dataclass
class Bots:
    bot_token: str
    admin_id: int

@dataclass
class Settings:
    bots: Bots

def get_setting(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str('BOT_TOKEN'),
            admin_id=env.int('MY_ID'),
        )
    )

def get_database(path: str):
    env = Env()
    env.read_env(path)

    return env('database')


setting = get_setting('.env')

database = get_database('.env')
