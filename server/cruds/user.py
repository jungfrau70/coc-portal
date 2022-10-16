from importlib.machinery import DEBUG_BYTECODE_SUFFIXES
from pyexpat import model
from sqlalchemy.orm import Session
from models.user import user
from schemas.user import UserRequest, UserResponse

# id = Column(Integer, primary_key=True, index=True)
# name = Column(String(255))
# email: Column(String(255))
# password: Column(String(255))

def create_user(db: Session, user: UserRequest):
    db_user = user(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# def read_users(db: Session, completed: bool):
    # if completed is None:
    #     return db.query(user).all()
    # else:
    #     return db.query(user).filter(user.completed == completed).all()
    
def read_users(db: Session):    
    return db.query(user).all()

def read_user(db: Session, id: int):
    return db.query(user).filter(user.id == id).first()

def update_user(db:Session, id: int, user: UserRequest):
    db_user = db.query(user).filter(user.id == id).first()
    if db_user is None:
        return None
    db.query(user).filter(user.id == id).update({
        'name': user.name,
        'completed': user.completed
    })
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db:Session, id: int):
    db_user = db.query(user).filter(user.id == id).first()
    if db_user is None:
        return None
    db.query(user).filter(user.id == id).delete()
    db.commit()
    return True
                   
