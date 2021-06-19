from typing import Optional
from sqlalchemy import Column, Text, String, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from database.core import TimeStampMixin, BaseSchema
from workshops.model import Workshop, presenter_workshop_association


class Presenter(Base, TimeStampMixin):
    __tablename__ = "presenters"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    phone = Column(String(80), unique=True, nullable=True)
    description = Column(Text, nullable=True)
    company = Column(String(140), nullable=True)
    title = Column(String(120), nullable=True)
    avatar = Column(String(100), default="default.png")
    website_url = Column(String(200), nullable=True)
    twitter_url = Column(String(200), nullable=True)
    facebook_url = Column(String(200), nullable=True)
    workshops = relationship(
        "Workshop", secondary=presenter_workshop_association, back_populates="lecturers"
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
