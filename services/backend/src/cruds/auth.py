from sqlalchemy.orm import Session
from cruds import models
from routers import schemas
from fastapi import HTTPException,status
from io import BytesIO

import pandas as pd
import numpy as np

from utils.hashing import Hash
from utils import token

Model = models.User
Schema = schemas.Auth


def register(request: Schema,db:Session):
    new_record = Model(
        name=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
        )
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

def login(request: Schema, db: Session):
    user = db.query(Model).filter(Model.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")
    access_token = token.create_access_token(data={"sub": user.email})   
    return { "access_token": access_token, "token_type": "bearer" }

def refresh(id:int,request, db:Session):
    user = db.query(Model).filter(Model.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")
    access_token = token.create_access_token(data={"sub": user.email})   
    return { "access_token": access_token, "token_type": "bearer" }


def show(id:int,request, db:Session):
    user = db.query(Model).filter(Model.email == request.username).first()    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"record with the id {id} is not available")
    return user    

