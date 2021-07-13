from datetime import datetime
from typing import Optional
from sqlalchemy import Column, String, Integer, DateTime, Text, Numeric
from sqlalchemy.orm import relationship
from database import Base
from database.core import StartEndDateMixin, StartEndDateSchema

from workshops.models import WorkshopRead
from conferences.models import ConferenceRead

# One event can have multiple relationships One to many


class Event(Base, StartEndDateMixin):
    __tablename__ = "events"
    """An Event Model that represents events table in the database"""

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, index=True)
    description = Column(Text)
    price = Column(Numeric)
    country = Column(String)
    city = Column(String)
    address = Column(String)

    # Relationships
    workshops = relationship("Workshop")
    conferences = relationship("Conference")


# Pydantic Models
class EventBase(StartEndDateSchema):
    name: str
    description: Optional[str] = None
    price: int
    country: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None


class EventRegister(EventBase):
    pass


class EventUpdate(EventBase):
    pass


class EventRead(EventBase):
    workshops: Optional[WorkshopRead] = None
    conferences: Optional[ConferenceRead] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
