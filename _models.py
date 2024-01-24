from pydantic import BaseModel, EmailStr
class Admin(BaseModel):    
    admin_id: int
    username: str
    password: str 
    email: EmailStr
