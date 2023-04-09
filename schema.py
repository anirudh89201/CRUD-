from pydantic import BaseModel,EmailStr;
import datetime;
class User(BaseModel):
    id:int
    Name:str
class UserCreate(BaseModel):
    email:EmailStr;
    password:str;
class UserOut(BaseModel):
    id:int;
    email:EmailStr;
    class Config:
        orm_mode=True; 