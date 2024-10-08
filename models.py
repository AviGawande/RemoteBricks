from pydantic import BaseModel, EmailStr

class UserRegistration(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class LinkID(BaseModel):
    user_id: str
    id_link: str
