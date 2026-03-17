from datetime import datetime

from pydantic import BaseModel


# Data received from user
class LinkCreate(BaseModel):
    title: str
    url: str


# Data send at user
class LinkOut(BaseModel):
    id: int
    title: str
    url: str
    created_at: datetime

    class Config:
        from_attributes = True
