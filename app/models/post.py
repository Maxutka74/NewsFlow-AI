import uuid
from datetime import datetime, timezone
from typing import Literal

from pydantic import BaseModel, Field


class Post(BaseModel):
    article_id: str
    title: str
    text: str
    status: Literal['pending', 'approved', 'rejected', 'published'] = 'pending'
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
