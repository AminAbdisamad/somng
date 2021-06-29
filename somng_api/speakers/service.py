from typing import Optional
from speakers.model import (
    PresenterRegister,
    PresenterRead,
    PresenterUpdate,
    Presenter,
)
from sqlalchemy.orm import Session
from database.core import save


def add_presenter(*, db: Session, presenter: PresenterRegister) -> Optional[Presenter]:
    """Create new presenter"""
    presenter = Presenter(**presenter.dict())
    save(db=db, data=presenter)
    return presenter


def get_presenter_by_id(db: Session, presenter_id: int) -> Optional[PresenterRead]:
    """Gets presenter by its id"""
    return db.query(Presenter).filter(Presenter.id == presenter_id).one_or_none()


def get_all_presenters(db: Session) -> list[Optional[Presenter]]:
    """Get all presenters"""
    return db.query(Presenter).all()
