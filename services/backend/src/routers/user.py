from typing import List, Union
from fastapi import APIRouter,Depends,status,HTTPException, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from pandas_ods_reader import read_ods

from config import database
from routers import schemas
from utils import oauth2
from sqlalchemy.orm import Session
from cruds import user

router = APIRouter(
    prefix="/auth",
    tags=['Users']
)

get_db = database.get_db

SchemaShow = schemas.ShowUser
Schema = schemas.User

@router.get('/all', response_model=List[SchemaShow])
# def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
def all(db: Session = Depends(get_db)):
    return user.get_all(db)

@router.get('/user', status_code=200, response_model=Schema)
# def show(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
def show(id:int, db: Session = Depends(get_db)):
    return user.show(id,db)

@router.get('/{id}', status_code=200, response_model=Schema)
# def show(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
def show(id:int, db: Session = Depends(get_db)):
    return user.show(id,db)    

@router.post('/login', status_code=status.HTTP_201_CREATED,)
# def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
def create(request: Schema, db: Session = Depends(get_db)):
    return user.login(request, db)

@router.post('/register', status_code=status.HTTP_201_CREATED,)
# def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
def create(request: Schema, db: Session = Depends(get_db)):
    return user.register(request, db)

@router.post('/refresh', status_code=status.HTTP_201_CREATED,)
# def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
def create(request: Schema, db: Session = Depends(get_db)):
    return user.refresh(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def destroy(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
def destroy(id:int, db: Session = Depends(get_db)):
    return user.destroy(id,db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
# def update(id:int, request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
def update(id:int, request: Schema, db: Session = Depends(get_db)):
    return user.update(id,request, db)