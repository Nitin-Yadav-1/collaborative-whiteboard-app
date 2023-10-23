
from datetime import datetime
from pydantic import BaseModel, EmailStr


class Whiteboard(BaseModel):
  id: int
  title: str
  created_at: datetime
  last_modified: datetime
  owner_id: int
  data: str | None = None
  thumbnail_image: str | None = None


class WhiteboardInfo(BaseModel):
  id: int
  title: str
  last_modified: datetime
  thumbnail_url: str
  shared_with: list[EmailStr]
  is_owner: bool


class WhiteboardCreate(BaseModel):
  title: str
  share_with: list[EmailStr] = []