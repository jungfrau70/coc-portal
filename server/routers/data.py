from typing import List
from fastapi import APIRouter,Depends,status,HTTPException, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from pandas_ods_reader import read_ods
from io import BytesIO, StringIO

from config import database
from routers import schemas
from utils import oauth2
from sqlalchemy.orm import Session
from cruds import blog, models

import csv, codecs, json
import pandas as pd

router = APIRouter(
    prefix="/data",
    tags=['Data']
)

get_db = database.get_db

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")

@router.get('/basic', response_class=HTMLResponse)
def get_basic_form(request: Request, db: Session = Depends(get_db)):  # , current_user: schemas.User = Depends(oauth2.get_current_user)):
    return templates.TemplateResponse( "basic-form.html", {"request": request})

@router.post('/basic', response_class=HTMLResponse)
async def get_basic_form(request: Request, username: str = Form(...), password: str = Form(...), file: UploadFile = File(...), db: Session = Depends(get_db)):  # , current_user: schemas.User = Depends(oauth2.get_current_user)):
    print(f'username: {username}')
    print(f'password: {password}')
    contents = file.file.read()
    data = BytesIO(contents)
    df = pd.read_csv(data)
    data.close()
    file.file.close()

    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # df_filtered = df[df['리전'].apply(lambda x: True if re.search(regex, str(x)) else False) & (df['테넌트']== 'PRD') & (df['진행상태']=='완료') & (df['월간']=='O')]

    for rows in df.iterrows():             
        print (rows)
    return templates.TemplateResponse( "basic-form.html", {"request": request})


@router.get('/awesome', response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("awesome-form.html", {"request": request})

@router.post('/awesome', response_class=HTMLResponse)
async def post_form(request: Request, form_data: schemas.AwesomeForm = Depends(schemas.AwesomeForm.as_form), db: Session = Depends(get_db)):
    print(f'username: {form_data.username}')
    print(f'password: {form_data.password}')
    contents = form_data.file.file.read()
    data = BytesIO(contents)
    df = pd.read_csv(data)
    data.close()
    form_data.file.file.close()

    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # for rows in df.iterrows():
    #     print (rows)

    try:
        json_data = df.to_json(orient='records')
        data = json.loads(json_data)

    # id = Column(Integer, primary_key=True, index=True)
    # year = df['년도']
    # month = df['월']
    # region = df['리전']
    # az = df['az']
    # tenant = df['tanent']
    # progress = df['진행상태']
    # impact = df['Impact_Severity']  
    # status = df['성패']
    # title = df['제목']
    # problem_desc = df['내용']
    # action_desc = df['작업']
    # action_person = df['작업자']
    # ticket_no = df['Ticket']
    # review_desc = df['ReviewResult']
    # review_date = datetime.datetime.now()
    # reviewer = "정인환" # df['Ticket']
    # rca_desc = df['Root_Cause']
    # creater = "정인환" # df['Ticket']
    # created_at = datetime.datetime.now()
    # updater = "정인환" # df['Ticket']
    # updated_at = datetime.datetime.now()

        for row in data:
            model = models.Task(**row)
            db.add(model)
    except:
        print("Sorry, some error has occurred!")

    return "Success"
    # return templates.TemplateResponse( "basic-form.html", {"request": request})


@router.get('/pyscript', response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("pyscript.html", {"request": request})

# @router.post('/', status_code=status.HTTP_201_CREATED,)
# def create(request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return blog.create(request, db)

# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def destroy(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return blog.destroy(id,db)


# @router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
# def update(id:int, request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return blog.update(id,request, db)


# @router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
# def show(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return blog.show(id,db)