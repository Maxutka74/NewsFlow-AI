import logging

from pymongo.errors import DuplicateKeyError

from app.db.mongodb import db
from app.models.article import Article

logger = logging.getLogger(__name__)

async def create_article(article: Article):
    data = article.model_dump()
    try:
        result = await db['articles'].insert_one(data)
        return result.inserted_id
    except DuplicateKeyError:
        logger.warning(f'Article %s already exists', article.url)


async def get_article_by_url(url: str):
    return await db['articles'].find_one({'url': url})

async def get_articles_by_source(source_id: str):
    data = db['articles'].find({'source_id': source_id})
    return [i async for i in data]