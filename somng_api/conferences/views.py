from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.core import get_db
from .models import Conference, ConferenceRead, ConferenceRegister, ConferenceUpdate
from conferences import services


conferences = APIRouter(prefix="/conference", tags=["conference"])


@conferences.post("/", response_model=ConferenceRegister)
async def add_event(conference: ConferenceRegister, db: Session = Depends(get_db)):
    return services.create_conference(db=db, conference=conference)


@conferences.get("/", response_model=list[Optional[ConferenceRead]])
async def get_conferences(
    db: Session = Depends(get_db),
) -> list[Optional[ConferenceRead]]:
    return services.get_conferences(db=db)


@conferences.get("/{id}")
async def get_conference_by_id(id: int, db: Session = Depends(get_db)):
    conference = services.get_conference_by_id(db=db, conference_id=id)
    if not conference:
        raise HTTPException(
            status_code=404, detail="A conference with this id does not exist."
        )
    return conference


@conferences.put("/{id}")
async def update_conference(
    id: int, conference_update: ConferenceUpdate, db=Depends(get_db)
):
    return services.update_conferences(
        db=db, id=id, conference_update=conference_update
    )


@conferences.delete("/{id}")
async def delete_conference(id: int, db: Session = Depends(get_db)):
    return services.remove_conference_by_id(db=db, id=id)
