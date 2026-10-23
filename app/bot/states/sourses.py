from aiogram.fsm.state import StatesGroup, State


class AddUrl(StatesGroup):
    url = State()