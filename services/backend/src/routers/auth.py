from typing import List, Union
from fastapi import APIRouter, Depends, status, HTTPException, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from pandas_ods_reader import read_ods

from config import database
from routers import schemas
from utils import oauth2
from sqlalchemy.orm import Session
from cruds import auth
from cruds.auth import (
    get_user_by_id_query,
    get_user_by_email_query,
    get_user_by_password_query,
    get_users_query,
    create_user_query,
    update_user,
    delete_user_query,
)
from auth.authentications import get_current_active_user
from auth import token

router = APIRouter(
    # prefix="/users",
    tags=['Auths']
)

get_db = database.get_db

from cruds.models import User
USER_MODEL = User

def get_authenticated_user(db: Session, email: str, password: str):
    """validate password and return user
    require: columns in conf.USER_MODEL
    - email
    - hashed_password
    """
    user = db.query(USER_MODEL).filter(USER_MODEL.email == email).first()
    if not user:
        return None
    if token.verify_password(password, user.hashed_password):
        return user


def get_token_data(user, token_schema):
    data = {"username": user.email}
    return token_schema(**data)


@router.post("/auth/token", response_model=schemas.Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    # form_data: schemas.FormData,
    db: Session = Depends(get_db),
):
    user = get_authenticated_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token_data = get_token_data(user, schemas.TokenData)
    access_token = token.add_access_token(token_data=token_data)
    return {"access_token": access_token}


# @router.post("/users/image/", response_model=schemas.User, tags=['user'])
# async def add_icon(
#     file: UploadFile = File(...),
#     db: Session = Depends(get_db),
#     current_user: schemas.User = Depends(get_current_active_user),
# ):
#     new_user = await process_image.save_and_add_icon(file, current_user.id, db)
#     return new_user


# @router.get("/users/friend/reflesh/invite_code/", response_model=schemas.User, tags=['user'])
# async def reflesh_invite_code(
#     db: Session = Depends(get_db),
#     current_user: schemas.User = Depends(get_current_active_user),
# ):
#     current_user = get_user_by_id_query(db, current_user.id)
#     return recreate_and_update_invite_code(db, current_user)


# @router.get("/users/friend/{invite_code}/", response_model=schemas.User, tags=['user'])
# async def add_friend(
#     invite_code: str,
#     db: Session = Depends(get_db),
#     current_user: schemas.User = Depends(get_current_active_user),
# ):
#     invitee = get_invitee(db, invite_code)
#     user, is_updated = append_friend(db, current_user, invitee)
#     if not is_updated:
#         raise HTTPException(status_code=400, detail="Already being friend")
#     return user

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

# SchemaShow = schemas.ShowAuth
# Schema = schemas.Auth


# @router.post('/register', status_code=status.HTTP_201_CREATED, response_model=Schema)
# # def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
# def create(request: schemas.User, db: Session = Depends(get_db)):
#     return auth.register(request, db)


# @router.post('/login', status_code=200, response_model=schemas.ShowUserToken)
# def login(request: Schema, db: Session = Depends(database.get_db)):
#     return auth.login(request, db)

# # @router.get('/user', status_code=200, response_model=SchemaShow)
# # # def show(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
# # def show(request: Schema, db: Session = Depends(get_db)):
# #     return auth.show(request.id,db)


# @router.post('/refresh', status_code=status.HTTP_201_CREATED,)
# # def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
# def create(request: Schema, db: Session = Depends(get_db)):
#     return auth.refresh(request, db)


# @router.get('/unprotected', status_code=200, response_model=SchemaShow)
# # def show(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
# def show(id: int, db: Session = Depends(get_db)):
#     return auth.show(id, db)


# @router.get('/protected', status_code=200, response_model=SchemaShow)
# # def show(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
# def show(id: int, db: Session = Depends(get_db)):
#     return auth.show(id, db)
