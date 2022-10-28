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


