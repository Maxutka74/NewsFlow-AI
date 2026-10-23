from aiogram.fsm.state import StatesGroup, State


class EditPost(StatesGroup):
    edit = State()