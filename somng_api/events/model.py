from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.orm import relationship
from database import Base
from database.core import TimeStampMixin, BaseSchema

# id :1
# name : 'SOMNOG 5 Event'
# startDate : 15 July
# EndDate : 20 July
# workshopTracks_id :
# ConferenceId :
# location:id
# price : 40

# One event can have multiple relationships One to many


class Event(Base, TimeStampMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, index=True)
    start_date = Column(DateTime, default=datetime.now)
    end_date = Column(DateTime, default=datetime.now)
    price = Column(Integer)
    workshop_id = None
    conference_id = None
    location_id = None
