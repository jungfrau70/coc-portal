from importlib.machinery import DEBUG_BYTECODE_SUFFIXES
from pyexpat import model
from sqlalchemy.orm import Session
from models.event import Event
from schemas import event

def create_event(db: Session, event: event.EventRequest):
    db_event = Event(name=event.name, completed=event.completed)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def read_events(db: Session, completed: bool):
    if completed is None:
        return db.query(Event).all()
    else:
        return db.query(Event).filter(Event.completed == completed).all()

def read_event(db: Session, id: int):
    return db.query(Event).filter(Event.id == id).first()

def update_event(db:Session, id: int, event: event.EventRequest):
    db_event = db.query(Event).filter(Event.id == id).first()
    if db_event is None:
        return None
    db.query(Event).filter(Event.id == id).update({
        'name': event.name,
        'completed': event.completed
    })
    db.commit()
    db.refresh(db_event)
    return db_event

def delete_event(db:Session, id: int):
    db_event = db.query(Event).filter(Event.id == id).first()
    if db_event is None:
        return None
    db.query(Event).filter(Event.id == id).delete()
    db.commit()
    return True
                   
