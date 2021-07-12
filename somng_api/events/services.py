from typing import Optional
from sqlalchemy.orm import Session
from .models import Event, EventRegister, EventRead, EventUpdate
from database.core import save
from datetime import datetime


def create_event(*, db: Session, event: EventRegister) -> Optional[Event]:
    """Adds Events to the database"""
    event = Event(**event.dict())
    save(db=db, data=event)
    return event


def get_events(*, db: Session) -> list[Optional[EventRead]]:
    """Get all events"""
    return db.query(Event).all()


def get_events_by_id(*, db: Session, event_id: int) -> Optional[Event]:
    """Gets Event by its id"""
    return db.query(Event).filter(Event.id == event_id).one_or_none()


def update_events(*, db: Session, event: EventUpdate, event_id: int):
    """Update events"""

    # get the existing data
    event_db = db.query(Event).filter(Event.id == event_id).one_or_none()
    if event_db is None:
        return None

    # Update model class variable from requested fields # **typo** was vars(db_user) => vars(user)
    for var, value in vars(event).items():
        setattr(event_db, var, value) if value else None

    event_db.updated_at = datetime.now()
    save(db=db, data=event_db)
    return event_db


def remove_events(*, db: Session, id: int) -> Event:
    """Delete Events"""
    event = db.query(Event).get(id)
    db.delete(event)
    db.commit()
    return event
