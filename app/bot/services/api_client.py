import httpx

class ApiClient:
    def __init__(self):
        self.client = httpx.AsyncClient(base_url='http://127.0.0.1:8000')

    async def close(self):
        await self.client.aclose()

    async def add_source(self, url: str):
        response = await self.client.post(
            url='/sources',
            json={
                'url': url,
                'type': 'website',
            },
        )

        return response

    async def get_articles(self):
        response = await self.client.get(
            url='/articles',
        )

        return response