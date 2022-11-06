from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from config import database
from config.database import engine

from cruds import models
from routers import user, blog, authentication
from routers import discussion_topic, incident_handling, issue_mgmt, problem_mgmt, change_mgmt, request_mgmt, asset_mgmt_database, asset_mgmt_kubernetes, asset_mgmt_instance, capacity_mgmt, backup_mgmt, security_mgmt, regular_check, license_mgmt, report

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
app.include_router(security_mgmt.router)
app.include_router(regular_check.router)
app.include_router(license_mgmt.router)
app.include_router(report.router)

# origins = [
#     "*"
# ]

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
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
async def http_exception_handler(request: Request, exc):
    print(f"{repr(exc)}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

app.mount("/static", StaticFiles(directory="static"), name="static")

# @lru_cache()
# def get_settings():
#     return Settings()


