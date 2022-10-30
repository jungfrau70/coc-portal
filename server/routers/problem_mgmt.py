from typing import List, Union
from fastapi import APIRouter,Depends,status,HTTPException, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from pandas_ods_reader import read_ods

from config import database
from routers import schemas
from utils import oauth2
from sqlalchemy.orm import Session
from cruds import models, problem_mgmt
from sqlalchemy.sql import func
from datetime import datetime

router = APIRouter(
    prefix="/problem",
    tags=['Problem Management']
)

get_db = database.get_db

Schema = schemas.ShowProblem

@router.get('/all', response_model=List[Schema])
# def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
def all(db: Session = Depends(get_db)):
    return problem_mgmt.get_all(db)

# @router.get('/all', response_model=List[Schema])
# # def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
# def all(db: Session = Depends(get_db)):
#     return problem.get_all(db)


# from fastapi.templating import Jinja2Templates
# templates = Jinja2Templates(directory="templates")

# @router.get('/upload-csv', response_class=HTMLResponse)
# def get_form(request: Request):
#     return templates.TemplateResponse("upload-csv.html", {"request": request})

# @router.get('/pyscript', response_class=HTMLResponse)
# def get_form(request: Request):
#     return templates.TemplateResponse("pyscript.html", {"request": request})

# @router.get('/all', status_code=200, response_model=List[Schema])
# def get_form(request: Request, db: Session = Depends(get_db)):
#     problems = pd.read_sql(db.query(models.Problem).statement,db.bind)
#     if problems.empty:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with the id {id} is not available")
#     return problems.to_json(orient='records')

@router.get('/{id}', status_code=200, response_model=Schema)
# def show(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
def show(id:int, db: Session = Depends(get_db)):
    return problem_mgmt.show(id,db)

@router.post('/', status_code=status.HTTP_201_CREATED,)
# def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return problem_mgmt.create(request, db)

# @router.post('/uploadfile', status_code=status.HTTP_201_CREATED,)
# async def post_form(request: Request, form_data: schemas.AwesomeForm = Depends(schemas.AwesomeForm.as_form), db: Session = Depends(get_db)):
@router.post('/uploadfile', status_code=status.HTTP_201_CREATED,)
async def upload_file(file: Union[UploadFile, None] = None, db: Session = Depends(get_db)):
    if file.filename.lower().endswith(('.csv')):
        return problem_mgmt.upload_csv(file, db)
    else:
        return {"message": "No csv upload file sent"}  

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def destroy(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
def destroy(id:int, db: Session = Depends(get_db)):
    return problem_mgmt.destroy(id,db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
# def update(id:int, request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
def update(id:int, request: schemas.Blog, db: Session = Depends(get_db)):
    return problem_mgmt.update(id,request, db)
