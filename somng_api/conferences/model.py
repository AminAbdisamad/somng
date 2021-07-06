from typing import Optional
from sqlalchemy import (
    Column,
    Text,
    String,
    Integer,
    Boolean,
    ForeignKey,
    DateTime,
)
from sqlalchemy.orm import relationship
from database import Base
from database.core import StartEndDateMixin, BaseSchema


class Conference(Base, StartEndDateMixin):
    __tablename__ = "conferences"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    location = Column(String)
    event_id = Column(Integer, ForeignKey("events.id"))
    # speakers_id = None
    # session_id = None
