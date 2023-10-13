
import mysql.connector

from .schema.user_schema import User

config = {
  "host" : "localhost",
  "user" : "python-app",
  "password" : "python-app",
  "database" : "collaborative_whiteboard"
}

db = None

def get_db():
  global db
  if db is None:
    db = mysql.connector.connect(**config)
  return db


def close_db():
  global db
  if db is not None:
    db.commit()
    db.close()
  db = None


def execute_query(query: str):
  db = get_db()
  cursor = db.cursor(named_tuple=True)
  cursor.execute(query)
  data = cursor.fetchall()
  cursor.close()
  close_db()
  return data


def get_user_by_email(email: str) -> User | None:
  query = f'''SELECT * FROM user WHERE email="{email}";'''
  data = execute_query(query)
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
  data = execute_query(query)
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
  execute_query(query)
  user = get_user_by_email(email)
  return user