from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from presenters.service import add_presenter, get_all_presenters, get_presenter_by_id
from database.core import get_db
from presenters.model import PresenterRegister, PresenterRead, Presenter

presenters = APIRouter(prefix="/api/v1/presenters")


@presenters.post("/")
def create_presenter(
    presenter: PresenterRegister, db: Session = Depends(get_db)
) -> Optional[Presenter]:
    return add_presenter(db=db, presenter=presenter)


@presenters.get("/")
def get_all(db: Session = Depends(get_db)) -> list[Optional[Presenter]]:
    return get_all_presenters(db=db)
