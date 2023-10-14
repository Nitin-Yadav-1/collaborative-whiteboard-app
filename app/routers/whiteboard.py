
import os

from dotenv import load_dotenv
from typing import Annotated
from fastapi import APIRouter, Depends

from app.dependencies.dependencies import get_user_id
from app.schema.whiteboard_schema import WhiteboardInfo
from app.models import whiteboard_model

load_dotenv()

DEFAULT_THUMBNAIL_URL = os.getenv("DEFAULT_THUMBNAIL_URL")

router = APIRouter(tags=["Whiteboard"])


@router.get("/whiteboards")
async def get_all_whiteboards(user_id: Annotated[int, Depends(get_user_id)]):
  whiteboards = whiteboard_model.get_whiteboards(user_id)
  result = []
  for board in whiteboards:
    is_owner = True if user_id == board.owner_id else False
    
    if board.thumbnail_image is None:
      thumbnail_url = DEFAULT_THUMBNAIL_URL

    shared_with = whiteboard_model.get_shared_emails(board.id)
    
    board_info = WhiteboardInfo(
      id=board.id,
      title=board.title,
      last_modified=board.last_modified,
      is_owner=is_owner,
      thumbnail_url=thumbnail_url,
      shared_with=shared_with
    )

    result.append(board_info)
  
  return result