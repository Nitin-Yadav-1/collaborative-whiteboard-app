'''
This module handles tasks related to JWT Token.
Token Payload is of the format : 
    {
      "user_id": <int>,
      "expire_time": <datetime string of format = "%Y%m%d%H%M%S">
    }
'''
import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
from jose import JWTError, jwt

load_dotenv()

SECRET_KEY = os.getenv('JWT_TOKEN_SECRET_KEY')
ALGORITHM = 'HS256'
TOKEN_EXPIRE_TIME_MINUTES = 5


def create_token(user_id: int) -> str:
  '''
  Creates a JWT token with payload as payload and an expire time.
  '''
  payload = create_payload(user_id)
  token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
  return token


def decode_token(token: str) -> dict | None:
  '''
  Decode the JWT token and return dict of payload.
  '''
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    expire_time = datetime.strptime(payload["expire_time"], "%Y%m%d%H%M%S")
    payload["expire_time"] = expire_time
  except JWTError:
    payload = None
  return payload


def create_payload(user_id: int) -> dict:
  '''
  Create a dict representing the payload of token.
  '''
  expire_time = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_TIME_MINUTES)
  payload = {
    "user_id": user_id,
    "expire_time": expire_time.strftime("%Y%m%d%H%M%S")
  }
  return payload

