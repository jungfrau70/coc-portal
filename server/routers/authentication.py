from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from config import database
from sqlalchemy.orm import Session
from . import schemas
from cruds import user

router = APIRouter(tags=['Authentication'])

@router.post('/account/login', status_code=200, response_model=schemas.Token)
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    return user.login(request,db)
