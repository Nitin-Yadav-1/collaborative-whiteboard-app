
from typing import Annotated
from fastapi import APIRouter, Depends, status

from app.dependencies.dependencies import get_user_id
from app.schema.whiteboard_schema import WhiteboardInfo, WhiteboardCreate
from app.models import whiteboard_model
from app.services import schema_converter

router = APIRouter(tags=["Whiteboard"])


@router.get("/whiteboards")
async def get_all_whiteboards(
  user_id: Annotated[int, Depends(get_user_id)]
) -> list[WhiteboardInfo]:
  '''
  Get all whiteboards for which the current user has access to.
  '''
  whiteboards = whiteboard_model.get_whiteboards(user_id)
  result = []
  for board in whiteboards:
    board_info = schema_converter.whiteboard_to_whiteboardinfo(board,user_id)
    result.append(board_info)
  return result


@router.post("/whiteboards", status_code=status.HTTP_201_CREATED)
async def create_whiteboard(
  whiteboard_create: WhiteboardCreate,
  user_id: Annotated[int, Depends(get_user_id)]
):
  '''
  Create new whiteboard with current user as its owner.
  '''
  new_board = whiteboard_model.create_whiteboard(whiteboard_create, user_id)
  board_info = schema_converter.whiteboard_to_whiteboardinfo(new_board, user_id)
  return board_info
  