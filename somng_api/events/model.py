from datetime import datetime
from typing import Optional
from sqlalchemy import Column, String, Integer, DateTime, Text
from sqlalchemy.orm import relationship
from database import Base
from database.core import StartEndDateMixin, BaseSchema


# One event can have multiple relationships One to many


class Event(Base, StartEndDateMixin):
    """An Event Model that represents events table in the database"""

    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, index=True)
    description = Column(Text)
    price = Column(Integer)
    country = Column(String, default="Somalia")
    city = Column(String, default="Mogadishu")
    address = Column(String)

    # Relationships
    workshops = relationship("Workshop")
    conferences = relationship("Conference")


# Pydantic Models
class EventBase(BaseSchema):
    name: str
    description: Optional[str] = None
    price: int
    country: str
    city: str
    address: Optional[str] = None


class EventRegister(EventBase):
    pass


class EventUpdate(EventBase):
    pass


class EventRead(EventBase):
    created_at: datetime
    updated_at: datetime
