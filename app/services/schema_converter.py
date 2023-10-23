
import os
from dotenv import load_dotenv

from app.models import whiteboard_model
from app.schema.whiteboard_schema import Whiteboard, WhiteboardInfo

load_dotenv()

DEFAULT_THUMBNAIL_URL = os.getenv("DEFAULT_THUMBNAIL_URL")


def whiteboard_to_whiteboardinfo(board: Whiteboard, user_id: int) -> WhiteboardInfo:
  '''
  Converts from 'Whiteboard' schema to 'WhiteboardInfo'.
  '''
  is_owner = ( user_id == board.owner_id )
    
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

  return board_info

