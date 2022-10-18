from distutils.command.config import config
# from functools import lru_cache
from typing import Union

from fastapi import FastAPI, Depends
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware

from routers import user, blog, authentication
from config.database import engine
from cruds import models

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(f"{repr(exc)}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# @lru_cache()
# def get_settings():
#     return Settings()


