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
from database.core import StartEndDateMixin, BaseSchema


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
    workshop_tracks = relationship("WorkshopTracks")


# * Pydantic Models
class PresenterBase(BaseSchema):
    first_name: str
    last_name: str
    email: str
    phone: str
    company: Optional[str]
    title: Optional[str]
    website_url: Optional[str]
    twitter_url: Optional[str]
    facebook_url: Optional[str]


class PresenterRegister(PresenterBase):
    avatar: Optional[str]


class PresenterUpdate(PresenterBase):
    avatar: Optional[str]


class PresenterRead(PresenterBase):
    id: int
    avatar: str
    Workshops: Optional[list[Workshop]]
