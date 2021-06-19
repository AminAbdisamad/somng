from datetime import datetime
from sqlalchemy import Column, DateTime
from pydantic import BaseModel
from enum import Enum
from sqlalchemy.orm import Session


class TimeStampMixin(object):
    """Timestamping mixin"""

    created_at = Column(DateTime, default=datetime.now)
    created_at._creation_order = 9998
    updated_at = Column(DateTime, default=datetime.now)
    updated_at._creation_order = 9998

    @staticmethod
    def _updated_at(mapper, connection, target):
        target.updated_at = datetime.now()


class BaseSchema(BaseModel):
    class Config:
        orm_mode = True
        validate_assignment = True
        arbitrary_types_allowed = True


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
