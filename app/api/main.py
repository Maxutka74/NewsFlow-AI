from fastapi import FastAPI
from app.api.routers.soursec import router as router_source
from app.api.routers.posts import router as router_news
from app.api.routers.articles import router as router_articles

app = FastAPI()
app.include_router(router_source)
app.include_router(router_news)
app.include_router(router_articles)
@app.get('/health')
async def health_check():
    return {'status': 'ok'}