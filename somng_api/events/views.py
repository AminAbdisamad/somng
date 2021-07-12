from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.core import get_db
from .models import Event, EventRead, EventRegister, EventUpdate
from events import services


events = APIRouter(
    prefix="/events",
    tags=["events"],
    responses={404: {"description": "Not found"}},
)


@events.post("/")
async def add_event(event: EventRegister, db: Session = Depends(get_db)):
    return services.create_event(db=db, event=event)


@events.get("/", response_model=list[Optional[EventRead]])
async def get_events(db: Session = Depends(get_db)):
    return services.get_events(db=db)


@events.get("/{event_id}")
async def get_event_by_id(event_id: int, db: Session = Depends(get_db)):
    return services.get_events_by_id(db=db, event_id=event_id)


@events.put("/{event_id}")
async def update_event(event_id: int, event_update: EventUpdate, db=Depends(get_db)):
    return services.update_events(db=db, event_id=event_id, event=event_update)


@events.delete("/{event_id}")
async def delete_event(event_id: int, db: Session = Depends(get_db)) -> Optional[Event]:
    return services.remove_events(db=db, id=event_id)
