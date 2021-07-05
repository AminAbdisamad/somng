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
from database.core import TimeStampMixin, BaseSchema


# * Database Models


# * Workshops and Presenters Association table
presenter_workshop_assoc = Table(
    "presenter_workshop_assoc",
    Base.metadata,
    Column("presenters_id", Integer, ForeignKey("presenters.id", ondelete="CASCADE")),
    Column("workshops_id", Integer, ForeignKey("workshops.id", ondelete="CASCADE")),
)


class Workshop(Base, TimeStampMixin):
    __tablename__ = "workshops"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    start_date = Column(DateTime, nullable=True, default=datetime.now)
    end_date = Column(DateTime, nullable=True, default=datetime.now)
    course_image = Column(String, nullable=False, default="default.png")
    location = Column(String)



# * Pydantic Models
class WorkshopBase(BaseSchema):
    title:str
    description:str
    start_date:Optional[datetime] = datetime.now()
    end_date:Optional[datetime] = datetime.now()
    course_image:str
    location:str


class PresenterRegister(PresenterBase):
    avatar: Optional[str]


class PresenterUpdate(PresenterBase):
    avatar: Optional[str]


class PresenterRead(PresenterBase):
    id: int
    avatar: str
    Workshops: Optional[list[Workshop]]
