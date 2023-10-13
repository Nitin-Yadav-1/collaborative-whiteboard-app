
from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends

from .. import model, tkn
from ..schema.user_schema import UserInfo
from ..dependencies import get_user_id


router = APIRouter(tags=['Users'])


@router.get("/user")
async def get_user_details(user_id: Annotated[int, Depends(get_user_id)]) -> UserInfo:
  user = model.get_user_by_id(user_id)

  if user is None:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      details="User does not exist"
    )

  return UserInfo(id=user.id, email=user.email)