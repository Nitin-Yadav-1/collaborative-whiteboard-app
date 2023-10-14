

from app.models import db
from app.schema.user_schema import User


def get_user_by_email(email: str) -> User | None:
  query = f'''SELECT * FROM user WHERE email="{email}";'''
  data = db.execute_query(query)
  user = None
  if len(data) == 1:
    row = data[0]
    user = User(
      id=row.id,
      email=row.email,
      password=row.password,
      created_at=row.created_at
    )
  return user


def get_user_by_id(user_id: int) -> User | None:
  query = f'''
    SELECT * FROM user WHERE id="{user_id}";
  '''
  data = db.execute_query(query)
  user = None
  if len(data) == 1:
    row = data[0]
    user = User(
      id=row.id,
      email=row.email,
      password=row.password,
      created_at=row.created_at
    )
  return user


def create_user(email: str, password: str) -> User | None:
  query = f'''
    INSERT INTO 
      user 
    (email, password) 
    values ("{email}", "{password}");
  '''
  db.execute_query(query)
  user = get_user_by_email(email)
  return user