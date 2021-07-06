from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Text, String, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from database.core import ContactMixin, ContactBase

# from workshops.model import Workshop, presenter_workshop_assoc


class Speaker(Base, ContactMixin):
    """Speakers Model represents speakers table in the database"""

    __tablename__ = "speakers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    description = Column(Text)
    company = Column(String(140), nullable=True)
    title = Column(String(120), nullable=True)
    avatar = Column(String(100), default="default.png")
    is_confirmed = Column(Boolean, default=False)
    session_id = None
    # workshops = relationship(
    #     "Workshop", secondary=presenter_workshop_assoc, back_populates="lecturers"
    # )


# * Pydantic Models
class SpeakerBase(ContactBase):
    name: str
    description: Optional[str] = None
    company: Optional[str] = None
    title: Optional[str] = None
    is_confirmed: Optional[bool] = False
    publish: Optional[bool] = False


class SpeakerRegister(SpeakerBase):
    pass


class SpeakerUpdate(SpeakerBase):
    pass


class SpeakerRead(SpeakerBase):
    id: int
    created_at: datetime
    updated_at: datetime
