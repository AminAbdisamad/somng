from typing import Optional
from sqlalchemy.orm import Session
from .models import Conference, ConferenceRegister, ConferenceRead, ConferenceUpdate
from database.core import save
from datetime import datetime


def create_conference(
    *, db: Session, conference: ConferenceRegister
) -> Optional[Conference]:
    """Adds Conferences to the database"""
    conference = Conference(**conference.dict())
    save(db=db, data=conference)
    return conference


def get_conferences(*, db: Session) -> list[Optional[Conference]]:
    """Get all Conferences"""
    return db.query(Conference).all()


def get_conference_by_id(*, db: Session, conference_id: int) -> Optional[Conference]:
    """Gets Conference by its id"""
    return db.query(Conference).filter(Conference.id == conference_id).one_or_none()


def update_conference(
    *, db: Session, conference_update: ConferenceUpdate, conference_id: int
) -> Optional[Conference]:
    """Update Conferences"""

    # get the existing data
    conference = (
        db.query(Conference).filter(Conference.id == conference_id).one_or_none()
    )
    if conference is None:
        return None

    # Update model class variable from requested fields # **typo** was vars(db_user) => vars(user)
    for var, value in vars(conference_update).items():
        setattr(conference_id, var, value) if value else None

    conference.updated_at = datetime.now()
    save(db=db, data=conference)
    return conference


def remove_conference_by_id(*, db: Session, id: int) -> Optional[Conference]:
    """Delete Conferences"""
    conference = db.query(Conference).get(id)
    db.delete(Conference)
    db.commit()
    return conference
