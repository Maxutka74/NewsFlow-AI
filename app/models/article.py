from datetime import datetime, timezone

from pydantic import BaseModel, Field


class Article(BaseModel):
    source_id: str
    url: str
    title: str
    content: str
    published_at: datetime | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))