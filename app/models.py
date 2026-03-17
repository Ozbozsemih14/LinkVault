from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from .database import Base


# This 'links' table base.
class Link(Base):
    __tablename__ = "links"  # Real name of databese table

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
