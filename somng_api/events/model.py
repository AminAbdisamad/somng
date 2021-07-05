from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Text
from sqlalchemy.orm import relationship
from database import Base
from database.core import StartEndDateMixin, BaseSchema

# id :1
# name : 'SOMNOG 5 Event'
# startDate : 15 July
# EndDate : 20 July
# workshopTracks_id :
# ConferenceId :
# location:id
# price : 40

# One event can have multiple relationships One to many


class Event(Base, StartEndDateMixin):
    """An Event Model that represents events table in the database"""

    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, index=True)
    description = Column(Text)
    price = Column(Integer)
    country = Column(String, default="Somalia")
    city = Column(String, default="Mogadishu")
    address = Column(String)

    workshop_id = None
    conference_id = None
