
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def validate(password: str, hashed_password: str) -> bool:
  '''
  Validates password against the given hashed_password by converting the 
  password to hashed_password and comparing them. Returns True if equal else 
  False.
  '''
  return pwd_context.verify(password, hashed_password)


def generate_hashed_password(password: str) -> str:
  '''
  Generates hashed password for the given plain password.
  '''
  return pwd_context.hash(password)