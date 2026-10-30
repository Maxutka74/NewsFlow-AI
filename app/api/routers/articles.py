from fastapi import APIRouter

from app.db.repositories.articles import get_articles_by_source, get_all_articles

router = APIRouter(prefix="/articles", tags=['Articles'])

@router.get('', status_code=200)
async def articles(source_id: str | None = None):
    if source_id:
        articles_result = await get_articles_by_source(source_id)
    else:
        articles_result = await get_all_articles()
    for article in articles_result:
        article['_id'] = str(article['_id'])

    return articles_result
