import asyncio

from aiogram import Bot, Dispatcher

from app.bot.handlers.moderation import router_moderation
from app.bot.handlers.news import router_news
from app.bot.handlers.sourses import router_url
from app.bot.handlers.start import router
from app.bot.middlewares.admin import AdminMiddleware
from app.core.config import BOT_TOKEN

dp = Dispatcher()
dp.update.outer_middleware(AdminMiddleware())
dp.include_router(router)
dp.include_router(router_url)
dp.include_router(router_news)
dp.include_router(router_moderation)

async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())