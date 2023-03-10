from typing import List, Union
from fastapi import APIRouter, Depends, status, HTTPException, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from pandas_ods_reader import read_ods

from config import database
from routers import schemas
from utils import oauth2
from sqlalchemy.orm import Session
from cruds import user
from cruds.user import (
    get_user_by_id_query,
    get_user_by_email_query,
    get_user_by_password_query,
    get_users_query,
    create_user_query,
    update_user,
    delete_user_query,
)

router = APIRouter(
    # prefix="/user",
    tags=['Users']
)

get_db = database.get_db

# SchemaShow = schemas.User
# Schema = schemas.User

from auth.authentications import get_current_active_user


@router.get("/users/", response_model=List[schemas.User])
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_active_user),
):
    db_user = get_users_query(db, skip=skip, limit=limit)
    if len(db_user) == 0:
        raise HTTPException(status_code=400, detail="User does not exist")
    return db_user


@router.post("/users/", response_model=schemas.User)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
    # current_user: schemas.User = Depends(get_current_active_user),
):
    db_user = get_user_by_email_query(db, email=user.email)
    # print(db_user.__dict__)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user_query(db=db, user=user)


@router.put("/users/", response_model=schemas.User)
def update_users(
    user: schemas.UserUpdate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_active_user),
):
    current_user = get_user_by_id_query(db, current_user.id)
    new_user, is_update = update_user(db, current_user, user)
    if not is_update:
        raise HTTPException(status_code=400, detail="only same value")
    return new_user


@router.delete("/users/", response_model=schemas.User)
def delete_user(
    user: schemas.UserDelete,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_active_user),
):
    db_user = get_user_by_password_query(
        db, email=user.email, password=user.password)

    if not db_user:
        raise HTTPException(status_code=400, detail="Does not exist")
    delete_user_query(db, db_user)
    return db_user


@router.get("/users/me/", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(get_current_active_user)):
    return current_user


# @router.get('/all', response_model=List[SchemaShow])
# # def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
# def all(db: Session = Depends(get_db)):
#     return user.get_all(db)


# @router.get('/{id}', status_code=200, response_model=Schema)
# # def show(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
# def show(id: int, db: Session = Depends(get_db)):
#     return user.show(id, db)


# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# # def destroy(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
# def destroy(id: int, db: Session = Depends(get_db)):
#     return user.destroy(id, db)


# @router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
# # def update(id:int, request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
# def update(id: int, request: Schema, db: Session = Depends(get_db)):
#     return user.update(id, request, db)
