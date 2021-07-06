from datetime import datetime
from sqlalchemy import (
    String,
    Integer,
    Column,
    Text,
    DateTime,
    ForeignKey,
    Table,
)
from typing import Optional
from sqlalchemy import Column, Text, String, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from database.core import StartEndDateMixin, StartEndDateSchema


# * Database Models


# * Workshops and Presenters Association table
# presenter_workshop_assoc = Table(
#     "presenter_workshop_assoc",
#     Base.metadata,
#     Column("presenters_id", Integer, ForeignKey("presenters.id", ondelete="CASCADE")),
#     Column("workshops_id", Integer, ForeignKey("workshops.id", ondelete="CASCADE")),
# )


class Workshop(Base, StartEndDateMixin):
    __tablename__ = "workshops"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    location = Column(String)
    # workshop_tracks = relationship("WorkshopTracks")
    event_id = Column(Integer, ForeignKey("events.id"))


# * Pydantic Models
class WorkshopBase(StartEndDateSchema):
    title: str
    description: str
    location: str


class WorkshopRegister(WorkshopBase):
    pass


class WorkshopUpdate(WorkshopBase):
    pass


class WorkshopRead(WorkshopBase):
    id: int
    created_at: datetime
    updated_at: datetime
