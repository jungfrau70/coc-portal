from typing import List, Union
from fastapi import APIRouter,Depends,status,HTTPException, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from pandas_ods_reader import read_ods

from config import database
from routers import schemas
from utils import oauth2
from sqlalchemy.orm import Session
from cruds import auth

router = APIRouter(
    prefix="/auth",
    tags=['Auths']
)

get_db = database.get_db

# class UserBase(BaseModel):
#     username: str
#     email: str
#     password: str

# class User(UserBase):
#     class Config():
#         orm_mode = True 

# class ShowUser(UserBase):
#     id: int
#     username: str
#     email: str

#     class Config():
#         orm_mode = True 

# class UserToken(UserBase):
#     email: str
#     password: str

#     class Config():
#         orm_mode = True 

# class ShowUserToken(UserBase):
#     id: int
#     email: str
#     password: str

#     class Config():
#         orm_mode = True 

SchemaShow = schemas.ShowAuth
Schema = schemas.Auth

@router.post('/register', status_code=status.HTTP_201_CREATED, response_model=Schema)
# def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
def create(request: schemas.User, db: Session = Depends(get_db)):
    return auth.register(request, db)

@router.post('/login', status_code=200, response_model=schemas.ShowUserToken)
def login(request: Schema, db: Session = Depends(database.get_db)):
    # record = auth.login(request,db)
    # print(record)
    # return record
    return auth.login(request,db)

@router.post('/refresh', status_code=status.HTTP_201_CREATED,)
# def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
def create(request: Schema, db: Session = Depends(get_db)):
    return auth.refresh(request, db)

@router.get('/unprotected', status_code=200, response_model=SchemaShow)
# def show(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
def show(id:int, db: Session = Depends(get_db)):
    return auth.show(id,db)    

@router.get('/protected', status_code=200, response_model=SchemaShow)
# def show(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
def show(id:int, db: Session = Depends(get_db)):
    return auth.show(id,db)        