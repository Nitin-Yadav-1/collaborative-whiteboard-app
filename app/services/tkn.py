
import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
from jose import JWTError, jwt

load_dotenv()

SECRET_KEY = os.getenv('JWT_TOKEN_SECRET_KEY')
ALGORITHM = 'HS256'
TOKEN_EXPIRE_TIME = 5


def create_token(payload: dict) -> str:
  '''
  Creates a JWT token with payload as payload and an expire time.
  '''
  data = payload.copy()
  expire_time = datetime.utcnow() + timedelta(seconds=TOKEN_EXPIRE_TIME)
  data.update({"expire-time": expire_time.strftime("%Y%m%d%H%M%S")})
  token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
  return token


def decode_token(token: str) -> dict | None:
  '''
  Decode the JWT token and return date in payload.
  '''
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
  except JWTError:
    payload = None
  return payload

