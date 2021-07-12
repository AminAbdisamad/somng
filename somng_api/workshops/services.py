from typing import Optional
from sqlalchemy.orm import Session
from .models import Workshop, WorkshopRegister, WorkshopRead, WorkshopUpdate
from database.core import save
from datetime import datetime


def create_workshop(*, db: Session, workshop: WorkshopRegister) -> Optional[Workshop]:
    """Adds Workshops to the database"""
    workshop = Workshop(**workshop.dict())
    save(db=db, data=workshop)
    return workshop


def get_workshops(*, db: Session) -> list[Optional[Workshop]]:
    """Get all Workshops"""
    return db.query(Workshop).all()


def get_workshop_by_id(*, db: Session, workshop_id: int) -> Optional[Workshop]:
    """Gets Workshop by its id"""
    return db.query(Workshop).filter(Workshop.id == workshop_id).one_or_none()


def update_workshops(*, db: Session, workshop: WorkshopUpdate, workshop_id: int):
    """Update Workshops"""

    # get the existing data
    workshop_db = db.query(Workshop).filter(Workshop.id == workshop_id).one_or_none()
    if workshop_db is None:
        return None

    # Update model class variable from requested fields # **typo** was vars(db_user) => vars(user)
    for var, value in vars(workshop).items():
        setattr(workshop_db, var, value) if value else None

    workshop_db.updated_at = datetime.now()
    save(db=db, data=workshop_db)
    return workshop_db


def remove_workshop_by_id(*, db: Session, id: int) -> Workshop:
    """Delete Workshops"""
    workshop = db.query(Workshop).get(id)
    db.delete(workshop)
    db.commit()
    return workshop
