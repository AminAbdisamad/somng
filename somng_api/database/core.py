from typing import Optional
from datetime import datetime
from sqlalchemy import Column, DateTime, String
from pydantic import BaseModel
from enum import Enum
from sqlalchemy.orm import Session
from database import SessionLocal


# Database Generator
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class TimeStampMixin:
    """Timestamp mixin"""

    created_at = Column(DateTime, default=datetime.now)
    created_at._creation_order = 9998
    updated_at = Column(DateTime, default=datetime.now)
    updated_at._creation_order = 9998

    @staticmethod
    def _updated_at(mapper, connection, target):
        target.updated_at = datetime.now()


class StartEndDateMixin(TimeStampMixin):
    """Start date & End date Mixin"""

    start_date = Column(DateTime, default=datetime.now)
    end_date = Column(DateTime, default=datetime.now)


class ContactMixin(TimeStampMixin):
    """Contact Mixin"""

    email = Column(String(120), unique=True, nullable=False)
    phone = Column(String(80), unique=True, nullable=True)
    website_url = Column(String(200), nullable=True)
    twitter_url = Column(String(200), nullable=True)
    facebook_url = Column(String(200), nullable=True)


class BaseSchema(BaseModel):
    class Config:
        orm_mode = True
        validate_assignment = True
        arbitrary_types_allowed = True


class ContactBase(BaseSchema):
    email: str
    phone: str
    website_url: Optional[str] = None
    twitter_url: Optional[str] = None
    facebook_url: Optional[str] = None


class UserRoles(str, Enum):
    organizer = "Organizer"
    admin = "Admin"
    user = "User"


# * Save Databse
def save(*, db: Session, data: str):
    """Save to the database"""
    db.add(data)
    db.commit()
    db.flush(data)
