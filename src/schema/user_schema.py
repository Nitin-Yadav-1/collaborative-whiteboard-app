
from datetime import datetime
from pydantic import BaseModel, EmailStr


class User(BaseModel):
  id: int
  email: EmailStr
  password: str
  created_at: datetime

class UserInfo(BaseModel):
  id: int
  email: EmailStr