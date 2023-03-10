import os
import jwt
import pytz
# from app.settings import configs as conf
from datetime import datetime, timedelta
from passlib.context import CryptContext
from routers import schemas

from dotenv import load_dotenv
load_dotenv()

JWT_SECRET_KEY: str = os.getenv("SECRET_KEY")
JWT_ALGORITHM: str = os.getenv("ALGORITHM")
JWT_EXPIRRE_KEY = os.getenv("JWT_EXPIRREKEY", "exp")
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv('JWT_ACCESS_TOKEN_EXPIRE_MINUTES', 30))
PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str):
    return PWD_CONTEXT.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return PWD_CONTEXT.hash(password)

def add_access_token(token_data: schemas.TokenData, expire_min=None) -> bytes:
    to_encode = token_data.dict()
    if expire_min is None:
        expire_min = JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    expire = datetime.utcnow() + timedelta(minutes=expire_min)
    to_encode.update({"exp": expire})
    data = schemas.TokenFullData(**to_encode)
    encoded_jwt = jwt.encode(data.dict(), JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt

def validate_access_token(access_token: str):
    payload = jwt.decode(access_token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
    token_full_data = schemas.TokenFullData(**payload)
    if token_full_data.exp >= datetime.now((pytz.utc)):
        return payload
