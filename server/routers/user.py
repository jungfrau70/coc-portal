from telnetlib import STATUS
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.user import UserRequest, UserResponse
from config.db import SessionLocal
import cruds

router = APIRouter(
    prefix="/users"
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
def create_user(user: UserRequest, db: Session = Depends(get_db)):
    user = cruds.user.create_user(db, user)
    return user

@router.get("", response_model=List[UserResponse])
def get_users(completed: bool = None, db: Session = Depends(get_db)):
    users = cruds.user.read_users(db, completed)
    return users

@router.get("/{id}")
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = cruds.user.read_user(db, id)
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return user

@router.put("/{id}")
def put_user_by_id(id: int, user: UserRequest, db: Session = Depends(get_db)):
    res = cruds.user.update_user(db, id, user)
    if res is None:
        raise HTTPException(status_code=404, detail="user not found")
    if res:
        return "Successfully updated"

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_user(id: int, db: Session = Depends(get_db)):
    res = cruds.user.delete_user(db, id)
    if res is None:
        raise HTTPException(status_code=404, detail="user not found")
    if res:
        return "Successfully deleted"

