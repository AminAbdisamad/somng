from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Text, String, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from database.core import ContactMixin, ContactBase

# from workshops.model import Workshop, presenter_workshop_assoc


class Lecturer(Base, ContactMixin):
    """
    Lecturer Model represents workshop lecturers table in the database
    Workshop Lecturers are engineers that teach different tracks of the workshop
    """

    __tablename__ = "lecturers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    description = Column(Text)
    company = Column(String(140), nullable=True)
    title = Column(String(120), nullable=True)
    avatar = Column(String(100), default="default.png")
    is_confirmed = Column(Boolean, default=False)
    workshop_tracks_id = None
    # workshops = relationship(
    #     "Workshop", secondary=presenter_workshop_assoc, back_populates="lecturers"
    # )


# * Pydantic Models
class LecturerBase(ContactBase):
    name: str
    description: Optional[str] = None
    company: Optional[str] = None
    title: Optional[str] = None
    is_confirmed: Optional[bool] = False


class LecturerRegister(LecturerBase):
    pass


class LecturerUpdate(LecturerBase):
    pass


class LecturerRead(LecturerBase):
    id: int
    created_at: datetime
    updated_at: datetime
