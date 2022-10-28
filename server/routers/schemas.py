from typing import List, Optional
from pydantic import BaseModel
from fastapi import Form, File, UploadFile
from datetime import date, time, datetime

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
    # username: str
    # password: str
    file: UploadFile

    @classmethod
    def as_form(
        cls,
        # username: str = Form(...),
        # password: str = Form(...),
        file: UploadFile = File(...)
    ):
        return cls(
            # username=username,
            # password=password,
            file=file
        )

class Problem(BaseModel):
    id: int
    year: int
    month: int
    region: str
    az: int
    tenant: str

    progress: str
    status: str
    impact: str

    occurred_at: datetime
    title: str
    problem_desc: str
    action_desc: str
    person_in_charge: str
    ticket_no: str

    rca_desc: str
    reviewed_at: datetime
    review_desc: str

    reviewer: str
    creator: str
    updater: str
    
    class Config():
        orm_mode = True    

class ShowProblem(BaseModel):
    id: int
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    progress: Optional[str]
    status: Optional[str]
    impact: Optional[str]

    occurred_at: Optional[datetime]
    title: Optional[str]
    problem_desc: Optional[str]
    action_desc: Optional[str]
    person_in_charge: Optional[str]
    ticket_no: Optional[str]

    rca_desc: Optional[str]
    reviewed_at: Optional[datetime]
    review_desc: Optional[str]

    reviewer: Optional[str]
    creator: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True    



    # year = Column(Integer, nullable=False)
    # month = Column(Integer, nullable=False)
    # region = Column(String, nullable=False)
    # az = Column(Integer, nullable=False)
    # tenant = Column(String, nullable=False)

    # progress = Column(String, nullable=True)
    # status = Column(String, nullable=True) 
    # impact = Column(String, nullable=True)   
    # occurred_at = Column(DateTime, default=datetime.now)    

    # title = Column(String, nullable=True) 
    # problem_desc = Column(String(length=3000), nullable=True)
    # action_desc = Column(String(length=3000), nullable=True) 
    # person_in_charge = Column(String, nullable=True)  # Engineer    
    # ticket_no = Column(String, nullable=True) 

    # rca_desc = Column(String(length=3000), nullable=True) 
    # review_desc = Column(String(length=3000), nullable=True) 
    # reviewed_at = Column(DateTime, default=None)

    # creator = Column(String, nullable=True)
    # reviewer = Column(String, nullable=True)     
    # updater = Column(String, nullable=True)         