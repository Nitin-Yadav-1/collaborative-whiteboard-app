
from typing import Annotated
from datetime import datetime, timedelta

from fastapi import Header, Depends, HTTPException, status

from . import tkn


def get_token(authorization: Annotated[str | None, Header()] = None) -> str:
  '''
  Checks the 'Authorization' header for values 'bearer <token>'.
  If token is present returns it.
  '''
  login_required_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Login required to access this route."
  )

  if authorization is None:
    raise login_required_exception

  values = authorization.split()

  if len(values) != 2:
    raise login_required_exception

  if values[0].lower() != 'bearer':
    raise login_required_exception

  token = values[1]
  return token


def get_user_id(token: Annotated[str, Depends(get_token)]) -> int:
  payload = tkn.decode_token(token)

  if payload is None:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Misformed credentials"
    )

  expire_time = datetime.strptime(payload['expire-time'], "%Y%m%d%H%M%S")
  current_time = datetime.utcnow()

  if current_time > expire_time:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Credentials expired"
    )

  return int(payload['user_id'])