from aiogram.fsm.state import StatesGroup, State


class StateTime(StatesGroup):
    GET_TIME = State()