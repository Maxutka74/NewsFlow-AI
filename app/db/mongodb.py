import asyncio

from pymongo import AsyncMongoClient

from app.core.config import MONGO_URI, MONGO_DB_NAME

client = AsyncMongoClient(MONGO_URI)

db = client[MONGO_DB_NAME]

async def create_indexes():
    await db['sources'].create_index('url', unique=True)
    await db['articles'].create_index('url', unique=True)

if __name__ == '__main__':
    asyncio.run(create_indexes())
