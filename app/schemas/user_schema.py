from pydantic import BaseModel, EmailStr

# Registration
class UserCreate(BaseModel):
    user_name: str
    user_email: EmailStr
    user_password: str

# Login
class UserLogin(BaseModel):
    user_email: EmailStr
    user_password: str
