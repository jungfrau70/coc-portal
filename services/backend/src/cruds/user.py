from sqlalchemy.orm import Session
from routers import schemas
from . import models
from fastapi import HTTPException,status
from utils.hashing import Hash
from utils import token

Model = models.User
Schema = schemas.ShowUser

def create(request: Schema,db:Session):
    new_user = Model(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login(request: Schema, db: Session):
    user = db.query(Model).filter(Model.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")
    access_token = token.create_access_token(data={"sub": user.email})   
    return { "access_token": access_token, "token_type": "bearer" }

def show(email:str,db:Session):
    user = db.query(Model).filter(Model.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the email {email} is not available")
    return user

def show2(id:int,db:Session):
    user = db.query(Model).filter(Model.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user    