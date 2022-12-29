from fastapi import APIRouter
from . import schemas
from config import database
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from cruds import user

router = APIRouter(
    prefix="/api/auth",
    tags=['Users']
)

get_db = database.get_db
Schema = schemas.ShowUser

@router.post('/all', response_model=schemas.ShowUser)
def create_user(request: Schema,db: Session = Depends(get_db)):
    return user.show(email,db)

@router.post('/register', response_model=schemas.ShowUser)
def create_user(request: Schema,db: Session = Depends(get_db)):
    return user.create(request,db)

@router.get('/{email}',response_model=schemas.ShowUser)
def get_user(email:str, db: Session = Depends(get_db)):
    return user.show(email,db)
    
@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    return user.show2(id,db)
