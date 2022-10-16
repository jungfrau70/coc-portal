from telnetlib import STATUS
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.event import EventRequest, EventResponse
from config.db import SessionLocal
import cruds

router = APIRouter(
    prefix="/events"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise        
    finally:
        db.close()

@router.post("", status_code=status.HTTP_201_CREATED)
def create_event(event: EventRequest, db: Session = Depends(get_db)):
    event = cruds.event.create_event(db, event)
    return event

@router.get("", response_model=List[EventResponse])
def get_events(completed: bool = None, db: Session = Depends(get_db)):
    events = cruds.event.read_events(db, completed)
    return events

@router.get("/{id}")
def get_event_by_id(id: int, db: Session = Depends(get_db)):
    event = cruds.event.read_event(db, id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.put("/{id}")
def put_event_by_id(id: int, event: EventRequest, db: Session = Depends(get_db)):
    res = cruds.event.update_event(db, id, event)
    if res is None:
        raise HTTPException(status_code=404, detail="Event not found")
    if res:
        return "Successfully updated"

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_event(id: int, db: Session = Depends(get_db)):
    res = cruds.event.delete_event(db, id)
    if res is None:
        raise HTTPException(status_code=404, detail="Event not found")
    if res:
        return "Successfully deleted"

