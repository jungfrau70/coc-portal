from importlib.machinery import DEBUG_BYTECODE_SUFFIXES
from pyexpat import model
from sqlalchemy.orm import Session
from models.event import event
from schemas.event import EventRequest, EventResponse


# id = Column(Integer, primary_key=True, index=True)
# title = Column(String(255))
# description: Column(String(255))
# action: Column(String(255))
# status: Column(String)


def create_event(db: Session, event: EventRequest):
    db_event = event(title=event.title, description=event.description, action=event.action, status=event.status)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

# def read_events(db: Session, completed: bool = False):
#     if completed is None:
#         return db.query(event).all()
#     else:
#         return db.query(event).filter(event.completed == completed).all()

def read_events(db: Session):    
    return db.query(event).all()

def read_event(db: Session, id: int):
    return db.query(event).filter(event.id == id).first()

def update_event(db: Session, id: int, event: EventRequest):
    db_event = db.query(event).filter(event.id == id).first()
    if db_event is None:
        return None
    db.query(event).filter(event.id == id).update({
        'title': event.name,
        'description': event.description,
        'action': event.action,
        'status': event.status,
    })
    db.commit()
    db.refresh(db_event)
    return db_event

def delete_event(db:Session, id: int):
    db_event = db.query(event).filter(event.id == id).first()
    if db_event is None:
        return None
    db.query(event).filter(event.id == id).delete()
    db.commit()
    return True
                   
