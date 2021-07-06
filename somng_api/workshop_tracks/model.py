from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from database.core import StartEndDateMixin


class WorkshopTrack(Base, StartEndDateMixin):
    __tablename__ = "workshop_tracks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    course_image = Column(String, nullable=False, default="default.png")
    location = Column(String)
    lecturers = relationship("Lecturer")
