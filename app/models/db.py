
import mysql.connector

_config = {
  "host" : "localhost",
  "user" : "python-app",
  "password" : "python-app",
  "database" : "collaborative_whiteboard"
}

_db = None

def get_db():
  global _db
  if _db is None:
    _db = mysql.connector.connect(**_config)
  return _db


def close_db():
  global _db
  if _db is not None:
    _db.commit()
    _db.close()
  _db = None


def execute_query(query: str):
  _db = get_db()
  cursor = _db.cursor(named_tuple=True)
  cursor.execute(query)
  data = cursor.fetchall()
  cursor.close()
  close_db()
  return data

