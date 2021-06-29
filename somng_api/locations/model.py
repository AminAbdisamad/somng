from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Text
from sqlalchemy.orm import relationship
from database import Base
from database.core import TimeStampMixin, BaseSchema


class Location(Base, TimeStampMixin):
    id = Column(Integer, primary_key=True)
    country = Column(String)
    city = Column(String)
    district = Column(String)
    address = Column(String)
    location = Column(String)
    workshop_id = None
    conference_id = None
    event_id = None
