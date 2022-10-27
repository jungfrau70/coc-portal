from typing import List
from fastapi import APIRouter,Depends,status,HTTPException, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from pandas_ods_reader import read_ods
from io import BytesIO, StringIO

from config import database
from routers import schemas
from utils import oauth2
from sqlalchemy.orm import Session
from cruds import models, problem
from sqlalchemy.sql import func
from datetime import datetime

import csv, codecs, json
import pandas as pd
import numpy as np
import re

router = APIRouter(
    prefix="/problem",
    tags=['Problem']
)

get_db = database.get_db

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")

@router.get('/upload-csv', response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("upload-csv.html", {"request": request})

@router.get('/pyscript', response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("pyscript.html", {"request": request})

@router.get('/all', response_model=List[schemas.ShowProblem])
# def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
def all(db: Session = Depends(get_db)):
    return problem.get_all(db)

# @router.get('/all', status_code=200, response_model=List[schemas.ShowProblem])
# def get_form(request: Request, db: Session = Depends(get_db)):
#     problems = pd.read_sql(db.query(models.Problem).statement,db.bind)
#     if problems.empty:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with the id {id} is not available")
#     return problems.to_json(orient='records')

@router.get('/{id}', status_code=200, response_model=schemas.ShowProblem)
# def show(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
def show(id:int, db: Session = Depends(get_db)):
    return problem.show(id,db)

@router.post('/', status_code=status.HTTP_201_CREATED,)
# def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return problem.create(request, db)

# @router.post("/uploadfiles/")
# async def create_upload_files(form_data: schemas.AwesomeForm = Depends(schemas.AwesomeForm.as_form), db: Session = Depends(get_db)):
#     return {"filenames": [file.filename for file in form_data]}
    # contents = await files.read()
    # df = pd.read_csv(file)
    # return HTMLResponse(content=content)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def destroy(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
def destroy(id:int, db: Session = Depends(get_db)):
    return problem.destroy(id,db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
# def update(id:int, request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
def update(id:int, request: schemas.Blog, db: Session = Depends(get_db)):
    return problem.update(id,request, db)
