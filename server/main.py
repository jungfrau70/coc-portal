from distutils.command.config import config
# from functools import lru_cache
from typing import Union

from fastapi import FastAPI, Depends, Request, Form, UploadFile, File
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from config import database
from routers import schemas
from utils import oauth2
from sqlalchemy.orm import Session
from cruds import models, problem
from sqlalchemy.sql import func
from datetime import datetime
from io import BytesIO, StringIO

from routers import user, blog, authentication, problem
from config.database import engine
from cruds import models
from fastapi import HTTPException,status


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(problem.router)

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

get_db = database.get_db

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(f"{repr(exc)}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

app.mount("/static", StaticFiles(directory="static"), name="static")

# @lru_cache()
# def get_settings():
#     return Settings()
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")

import pandas as pd
import numpy as np

@app.post('/file-drag-drop', status_code=status.HTTP_201_CREATED,)
async def post_form(request: Request, form_data: schemas.AwesomeForm = Depends(schemas.AwesomeForm.as_form), db: Session = Depends(get_db)):
    contents = form_data.file.file.read()
    data = BytesIO(contents)
    df = pd.read_csv(data)

    df['reviewed_at'] = df['reviewed_at'].fillna(np.nan).replace([np.nan], ['1970-01-01'])
    df['reviewed_at'] = pd.to_datetime(df['reviewed_at'])
         
    data.close()
    form_data.file.file.close()
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # print(df)
    try:
        dicts = df.to_dict(orient='records')
        db.bulk_insert_mappings(models.Problem, dicts)        
        db.commit()
    except Exception as e:
        print(e)
        print("Sorry, some error has occurred!")

    return "Success"
    # return templates.TemplateResponse( "upload-csv.html", {"request": request})
    # return RedirectResponse("http://localhost:3000/problem")
