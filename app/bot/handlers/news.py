import httpx
from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.bot.services.api_client import ApiClient

router_news = Router()

@router_news.callback_query(F.data == 'view_news')
async def view_news(callback: CallbackQuery, api_client: ApiClient):
    await callback.answer()

    try:
        response = await api_client.get_articles()

        if response.status_code == 200:
            articles = response.json()

            if not articles:
                await callback.message.answer('📰 Новин поки немає')
                return

            text = '📰 Останні новини:\n'

            for index, article in enumerate(articles[:10], start=1):
                title = article['title']

                text += f'{index}. {title}\n'

            await callback.message.answer(text)

        else:
            await callback.message.answer('❌ Помилка сервера')

    except httpx.RequestError:
        await callback.message.answer('❌ API тимчасово недоступний')
        return