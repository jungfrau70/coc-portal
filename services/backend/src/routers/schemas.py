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

# class Problem(BaseModel):
#     id: int
#     year: int
#     month: int
#     region: str
#     az: int
#     tenant: str

#     progress: str
#     status: str
#     impact: str

#     occurred_at: datetime
#     title: str
#     problem_desc: str
#     action_desc: str
#     person_in_charge: str
#     ticket_no: str

#     rca_desc: str
#     reviewed_at: datetime
#     review_desc: str

#     reviewer: str
#     creator: str
#     updater: str
    
#     class Config():
#         orm_mode = True  

# # https://stackoverflow.com/a/60670614
# class AwesomeForm(BaseModel):
#     # username: str
#     # password: str
#     file: UploadFile

#     @classmethod
#     def as_form(
#         cls,
#         # username: str = Form(...),
#         # password: str = Form(...),
#         file: UploadFile = File(...)
#     ):
#         return cls(
#             # username=username,
#             # password=password,
#             file=file
#         )

class ShowDiscussion(BaseModel):
    id: int
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    progress: Optional[str]
    status: Optional[str]

    progress: Optional[str]
    status: Optional[str]
    discussion_topic: Optional[str]

    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True      


class ShowIncident(BaseModel):
    id: int
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    shift_start_date: Optional[date]
    shift_type: Optional[str]

    level_1_engineer1: Optional[str]
    level_1_engineer2: Optional[str]
    level_2_engineers: Optional[str]
    how_to_share: Optional[str]

    event: Optional[str]
    action: Optional[str]
    status: Optional[str]
    ticket_no: Optional[str]
    escalated_to_l3: Optional[str]
    comment: Optional[str]

    occurred_at: Optional[datetime]
    acknowledged_at: Optional[datetime]
    propogated_at: Optional[datetime]
    resolved_at: Optional[datetime]

    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True      


class ShowIssue(BaseModel):
    id: int
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    progress: Optional[str]
    status: Optional[str]

    title: Optional[str]
    description: Optional[str]
    action: Optional[str]

    occurred_at: Optional[datetime]
    resloved_at: Optional[datetime]

    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

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


    # year = Column(Integer, nullable=False)
    # month = Column(Integer, nullable=False)
    # region = Column(String, nullable=False)
    # az = Column(Integer, nullable=False)
    # tenant = Column(String, nullable=False)

    # vendor = Column(String, nullable=True)
    # license_type = Column(String, nullable=True)     
    # status = Column(String, nullable=True)
    # instance_name = Column(String, nullable=True)
    # installed_at = Column(String, nullable=True)     
    # comment = Column(String(length=3000), nullable=True) 

    # creator = Column(String, nullable=True)
    # reviewer = Column(String, nullable=True)     
    # updater = Column(String, nullable=True) 

    occurred_at: Optional[datetime]
    title: Optional[str]
    description: Optional[str]
    action: Optional[str]
    person_in_charge: Optional[str]
    ticket_no: Optional[str]

    rca_desc: Optional[str]
    reviewed_at: Optional[datetime]
    review_desc: Optional[str]

    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True    


class ShowChange(BaseModel):
    id: int
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    progress: Optional[str]
    status: Optional[str]

    ticket_no: Optional[str]
    title: Optional[str]
    description: Optional[str]

    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True  


class ShowRequest(BaseModel):
    id: int
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    progress: Optional[str]
    status: Optional[str]

    ticket_no: Optional[str]
    title: Optional[str]
    description: Optional[str]
    work_type: Optional[str]

    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True  


class ShowCapacity(BaseModel):
    id: int
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    progress: Optional[str]
    status: Optional[str]

    category: Optional[str]
    ticket_no: Optional[str]
    title: Optional[str]
    description: Optional[str]

    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True   


class ShowBackup(BaseModel):
    id: int
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    progress: Optional[str]
    status: Optional[str]

    db_type: Optional[str]
    instance_name: Optional[str]
    instance_ip: Optional[str]
    freq_full_archive: Optional[str]
    comment: Optional[str]

    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True     


class ShowSecurity(BaseModel):
    id: int
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    progress: Optional[str]
    status: Optional[str]

    ticket_no: Optional[str]
    title: Optional[str]
    task_type: Optional[str]

    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True   


class ShowLicense(BaseModel):
    id: int
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    vendor: Optional[str]
    license_type: Optional[str]
    status: Optional[str]
    instance_name: Optional[str]
    installed_at: Optional[str]
    comment: Optional[str]

    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True     


class ShowDatabase(BaseModel):
    id: int
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    db_type: Optional[str]
    count: Optional[int]

    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True      

class ShowKubernetes(BaseModel):
    id: int
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    status: Optional[str]
    cluster_name: Optional[str]
    node_type: Optional[str]
    node_name: Optional[str]
    node_ips: Optional[str]
    api_vip: Optional[str]
    flavor: Optional[str]
    network_zone: Optional[str]
    contacts: Optional[str]
    k8s_version: Optional[str]
    monitoring_agent: Optional[str]

    api_cert_expired_date: Optional[datetime]
    ca_cert_expired_date: Optional[datetime]
    etcd_cert_expired_date: Optional[datetime]

    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True      

class ShowInstance(BaseModel):
    id: int
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    count: Optional[int]
    status: Optional[str]

    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True      


class ShowRegularCheck(BaseModel):
    id: int
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    progress: Optional[str]
    status: Optional[str]

    freq: Optional[str]
    vendor: Optional[str]
    title: Optional[str]
    description: Optional[str]

    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True   


class ShowReport(BaseModel):
    id: int
    year: Optional[int]
    month: Optional[int]
    region: Optional[str]
    az: Optional[int]
    tenant: Optional[str]

    progress: Optional[str]
    status: Optional[str]

    vendor: Optional[str]
    report_name: Optional[str]
    comment: Optional[str]

    creator: Optional[str]
    reviewer: Optional[str]
    updater: Optional[str]

    class Config():
        orm_mode = True      
