from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.bot.keyboards.moderation import moderation_keyboard

router_news = Router()

@router_news.callback_query(F.data == 'view_news')
async def view_news(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('📰 Перегляд новин поки недоступний. Функціонал буде активовано після підключення бази даних.'
                                  , reply_markup=moderation_keyboard(post_id='abc')
                                  )