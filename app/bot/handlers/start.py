from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.bot.keyboards.main import main_keyboard

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer('👋 Вітаємо в NewsFlow-AI!\n'
                         '🤖 Система автоматичного збору, обробки та публікації новин за допомогою штучного інтелекту.\n'
                         'Оберіть потрібну дію нижче 👇', reply_markup=main_keyboard())
