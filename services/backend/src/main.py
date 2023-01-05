import os

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

load_dotenv()

from config import database
from config.database import engine

from cruds import models
from routers import user, blog, authentication
from routers import discussion_topic, incident_handling, issue_mgmt, problem_mgmt, change_mgmt, request_mgmt, asset_mgmt_database, asset_mgmt_kubernetes, asset_mgmt_instance, asset_mgmt_license, capacity_mgmt, backup_mgmt, preventive, vulnerability, report

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog.router)

app.include_router(discussion_topic.router)
app.include_router(incident_handling.router)
app.include_router(issue_mgmt.router)
app.include_router(problem_mgmt.router)
app.include_router(change_mgmt.router)
app.include_router(request_mgmt.router)
app.include_router(asset_mgmt_database.router)
app.include_router(asset_mgmt_kubernetes.router)
app.include_router(asset_mgmt_instance.router)
app.include_router(capacity_mgmt.router)
app.include_router(backup_mgmt.router)
app.include_router(vulnerability.router)
app.include_router(preventive.router)
app.include_router(asset_mgmt_license.router)
app.include_router(report.router)

origins = [
    "http://localhost:80",
    os.environ['Front_BaseURL'],
]

# origins = [
#     "http://localhost:3000",
#     "http://localhost:8000",  
#     "http://192.168.30.254:3000",
#     "http://192.168.30.254:8000", 
# ]
SQLALCHEMY_DATABASE_URL =  f"postgresql+psycopg2://{os.environ['DATABASE_USER']}:{os.environ['DATABASE_PASSWORD']}@{os.environ['DATABASE_HOST']}:{os.environ['DATABASE_PORT']}/{os.environ['DATABASE_NAME']}"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

get_db = database.get_db

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc):
    print(f"{repr(exc)}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

app.mount("/static", StaticFiles(directory="static"), name="static")

# @lru_cache()
# def get_settings():
#     return Settings()


