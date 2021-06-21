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
from sqlalchemy.orm import relationship
from database import Base
from database.core import TimeStampMixin


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
    title = Column(String(150), nullable=False)
    description = Column(Text)
    start_date = Column(DateTime, nullable=True, default=datetime.now)
    end_date = Column(DateTime, nullable=True, default=datetime.now)
    course_image = Column(String(20), nullable=False, default="default.png")
    location = Column(String(80))
    presenters = relationship(
        "Presenters",
        secondary=presenter_workshop_assoc,
        back_populates="workshops",
    )
