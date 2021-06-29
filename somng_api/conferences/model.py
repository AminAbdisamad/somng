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
from workshops.model import Workshop, presenter_workshop_assoc


class Conference(Base, StartEndDateMixin):
    __tablename__ = "conferences"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(Text)
    location_id = None
    speakers_id = None
    session_id = None
