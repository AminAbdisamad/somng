from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.core import get_db
from .models import Workshop, WorkshopRead, WorkshopRegister, WorkshopUpdate
from workshops import services


workshops = APIRouter(
    prefix="/workshops",
    tags=["workshops"],
    responses={404: {"description": "Not found"}},
)


@workshops.post("/")
async def add_workshop(
    workshop: WorkshopRegister, db: Session = Depends(get_db)
) -> Optional[Workshop]:
    return services.create_workshop(db=db, workshop=workshop)


@workshops.get("/", response_model=list[WorkshopRead])
async def get_workshops(db: Session = Depends(get_db)):
    return services.get_workshops(db=db)


@workshops.get("/{id}")
async def get_event_by_id(id: int, db: Session = Depends(get_db)):
    return services.get_workshop_by_id(db=db, workshop_id=id)


@workshops.put("/{id}")
async def update_workshop(id: int, workshop: WorkshopUpdate, db=Depends(get_db)):
    return services.update_workshops(db=db, workshop_id=id, workshop=workshop)


@workshops.delete("/{id}")
async def delete_workshop(id: int, db: Session = Depends(get_db)) -> Optional[Workshop]:
    return services.remove_workshop_by_id(db=db, id=id)
