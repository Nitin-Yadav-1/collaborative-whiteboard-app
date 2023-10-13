
from datetime import datetime, timedelta
from jose import JWTError, jwt


SECRET_KEY = '74e3b817b97dcce5a049d2111eca900b2a748b6f52984af16e4a787149dffdd3'
ALGORITHM = 'HS256'
TOKEN_EXPIRE_TIME = 5


def create_token(payload: dict) -> str:
  '''
  Creates a JWT token with payload as payload and an expire time.
  '''
  data = payload.copy()
  expire_time = datetime.utcnow() + timedelta(seconds=TOKEN_EXPIRE_TIME)
  data.update({"expire-time": str(expire_time)})
  token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
  return token


def decode_token(token: str) -> dict | None:
  '''
  Decode the JWT token and return date in payload.
  '''
  payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
  return payload

