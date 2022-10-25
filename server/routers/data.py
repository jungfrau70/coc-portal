from typing import List
from fastapi import APIRouter,Depends,status,HTTPException, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse

from config import database
from routers import schemas
from utils import oauth2
from sqlalchemy.orm import Session
from cruds import blog

import csv, codecs

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
    content = await file.read()
    
    print(content)
    return templates.TemplateResponse( "basic-form.html", {"request": request})


@router.get('/awesome', response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("awesome-form.html", {"request": request})

@router.post('/awesome', response_class=HTMLResponse)
async def post_form(request: Request, form_data: schemas.AwesomeForm = Depends(schemas.AwesomeForm.as_form)):
    # print(form_data)
    print(form_data.username)
    print(form_data.password)
    file = form_data.file

    csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
    data = {}
    for rows in csvReader:             
        # key = rows['Id']  # Assuming a column named 'Id' to be the primary key
        # data[key] = rows  
        print (rows)
    
    file.file.close()

    # return templates.TemplateResponse( "basic-form.html", {"request": request})

    return templates.TemplateResponse("awesome-form.html", {"request": request})

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