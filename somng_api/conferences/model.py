from typing import Optional
from sqlalchemy import Column, Text, String, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from database.core import TimeStampMixin, BaseSchema
from workshops.model import Workshop, presenter_workshop_assoc


class Speaker(Base, TimeStampMixin):
    __tablename__ = "speakers"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    company = Column(String(140), nullable=True)
    title = Column(String(120), nullable=True)
    avatar = Column(String(100), default="default.png")
    workshops = relationship(
        "Workshop", secondary=presenter_workshop_assoc, back_populates="lecturers"
    )


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
