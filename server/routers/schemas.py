from typing import List, Optional
from pydantic import BaseModel
from fastapi import Form, File, UploadFile

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    blogs : List[Blog] =[]
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body:str
    creator: ShowUser

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None


# https://stackoverflow.com/a/60670614
class AwesomeForm(BaseModel):
    username: str
    password: str
    file: UploadFile

    @classmethod
    def as_form(
        cls,
        username: str = Form(...),
        password: str = Form(...),
        file: UploadFile = File(...)
    ):
        return cls(
            username=username,
            password=password,
            file=file
        )

class Problem(BaseModel):
    id: int
    year: str
    month: str
    region: str
    az: str
    tenant: str

    progress: str
    status: str
    impact: str

    occurred_at: str
    title: str
    problem_desc: str
    action_desc: str
    person_in_charge: str
    ticket_no: str

    rca_desc: str
    review_date: str
    review_desc: str
    reviewer: str

    creator: str
    updater: str
    
    class Config():
        orm_mode = True    

class ShowProblem(BaseModel):
    id: int
    year: str
    month: str
    region: str
    az: str
    tenant: str

    progress: str
    status: str
    impact: str

    occurred_at: str
    title: str
    problem_desc: str
    action_desc: str
    person_in_charge: str
    ticket_no: str

    rca_desc: str
    review_date: str
    review_desc: str
    reviewer: str

    creator: str
    updater: str

    class Config():
        orm_mode = True    