import httpx
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.bot.keyboards.main import cancel_button
from app.bot.services.api_client import ApiClient
from app.bot.states.sourses import AddUrl

router_url = Router()

@router_url.callback_query(F.data == 'add_url')
async def add_url(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('🔗 Надішліть URL новинного сайту, який хочете додати до системи', reply_markup=cancel_button('Скасування'))
    await state.set_state(AddUrl.url)

@router_url.message(AddUrl.url)
async def post_add_url(message: Message, state: FSMContext, api_client: ApiClient):
    url = message.text

    if not url:
        await message.answer('❌ Надішліть URL текстовим повідомленням')
        return

    try:
        response = await api_client.add_source(url)

        if response.status_code == 201:
            await message.answer('✅ URL успішно доданий')
            await state.clear()

        elif response.status_code == 409:
            await message.answer('⚠️ Такий URL уже існує')
            await state.clear()

        elif response.status_code == 422:
            await message.answer('❌ Некоректні дані джерела')

        else:
            await message.answer('❌ Сталася помилка сервера')

    except httpx.RequestError:
        await message.answer('❌ API тимчасово недоступний')
        return

@router_url.callback_query(AddUrl.url, F.data == 'cancel_url')
async def cancel_url(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('❌ Додавання URL скасовано')
    await state.clear()
    await callback.message.edit_reply_markup(reply_markup=None)