import asyncio
import logging

from pymongo.errors import DuplicateKeyError

from app.db.mongodb import db
from app.models.sourse import Source

logger = logging.getLogger(__name__)

async def create_source(source: Source):
    data = source.model_dump()
    try:
        result = await db['sources'].insert_one(data)
        return result.inserted_id
    except DuplicateKeyError:
        logger.warning('Source %s already exists', source.url)

async def get_source_by_url(url: str):
    return await db['sources'].find_one({'url': url})

async def get_all_sources():
    data = db['sources'].find()
    return [i async for i in data]

async def update_source_status(url: str, is_active: bool):
    change_post = await db['sources'].update_one({'url': url}, {'$set': {'is_active': is_active}})
    return change_post.modified_count

async def delete_source(url: str):
    delete_post = await db['sources'].delete_one({'url': url})
    return delete_post.deleted_count

if __name__ == '__main__':
    source = Source(url="https://example.com", type="website")
    asyncio.run(create_source(source))