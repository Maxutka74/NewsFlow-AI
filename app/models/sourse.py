from datetime import datetime, timezone
from typing import Literal

from pydantic import BaseModel, Field


class Source(BaseModel):
    url: str
    type: Literal["website", 'telegram']
    is_active: bool = True
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))