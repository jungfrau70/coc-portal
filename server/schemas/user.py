from pydantic import BaseModel

class UserRequest(BaseModel):
    id: int
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
            