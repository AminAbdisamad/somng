from typing import Optional
from sqlalchemy.orm import Session
from .models import Event, EventRegister, EventRead, EventUpdate
from database.core import save


def create_event(*, db: Session, event: EventRegister) -> Optional[Event]:
    """Adds Events to the database"""
    event = Event(**event.dict())
    save(db=db, data=event)
    return event


def get_events(*, db: Session) -> list[Optional[Event]]:
    """Get all events"""
    return db.query(Event).all()


def get_events_by_id(db: Session, event_id: int) -> Optional[Event]:
    """Gets Event by its id"""
    return db.query(Event).filter(Event.id == event_id).one_or_none()
