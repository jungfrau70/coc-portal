from sqlalchemy.orm import Session
from cruds import models
from routers import schemas
from fastapi import HTTPException, status
from io import BytesIO
from datetime import datetime

import pandas as pd
import numpy as np

from utils.hashing import Hash
from utils import token

from auth.token import verify_password, get_password_hash

Model = models.User
Schema = schemas.User


def get_all(db: Session):
    records = db.query(Model).all()
    return records


def get(id: int, request, db: Session):
    record = db.query(Model).filter(Model.email == request.email).first()
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"record with the id {id} is not available")
    return record


def destroy(id: int, db: Session):
    record = db.query(Model).filter(Model.id == id)

    if not record.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"record with id {id} not found")

    # record.delete(synchronize_session=False)
    db.query(Model).filter(Model.id == id).delete()
    db.commit()
    return 'done'


def update(id: int, request, db: Session):
    record = db.query(Model).filter(Model.id == id).first()
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"record with id {id} not found")

    db.query(Model).filter(Model.id == id).update({
        "username": request.username,
        "email": request.email,
    })
    db.commit()
    db.refresh(record)
    return 'updated'


def show(id: int, db: Session):
    record = db.query(Model).filter(Model.id == id).first()
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"record with the id {id} is not available")
    return record

###########################

def get_user_by_id_query(db: Session, user_id: int):
    """get user by user id"""
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email_query(db: Session, email: str):
    """get user by email"""
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_password_query(db: Session, email: str, password: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def get_users_query(db: Session, skip: int = 0, limit: int = 100):
    """get user list"""
    return db.query(models.User).order_by(models.User.id.desc()).offset(skip).limit(limit).all()

def create_user_query(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        email=user.email, username=user.username, hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, base_user: models.User, user: schemas.UserUpdate):
    is_update = base_user.update_dict({key: val for key, val in user.dict().items() if val is not None})
    if is_update:
        db.commit()
        db.refresh(base_user)
    return base_user, is_update

def delete_user_query(db: Session, user: Session.query):
    db.delete(user)
    db.commit()


