from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.bot.keyboards.main import cancel_button
from app.bot.states.sourses import AddUrl

router_url = Router()

@router_url.callback_query(F.data == 'add_url')
async def add_url(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('🔗 Надішліть URL новинного сайту, який хочете додати до системи', reply_markup=cancel_button('Скасування'))
    await state.set_state(AddUrl.url)

@router_url.message(AddUrl.url)
async def post_add_url(message: Message, state: FSMContext):
    await message.answer('URL Успішно доданий')
    await state.clear()

@router_url.callback_query(AddUrl.url, F.data == 'cancel_url')
async def cancel_url(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('❌ Додавання URL скасовано')
    await state.clear()
    await callback.message.edit_reply_markup(reply_markup=None)