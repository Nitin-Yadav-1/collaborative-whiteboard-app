
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

_config = {
  "host" : os.getenv("DB_HOST"),
  "user" : os.getenv("DB_USER"),
  "password" : os.getenv("DB_PASSWORD"),
  "database" : os.getenv("DB_DATABASE")
}

_db = None

def _get_db():
  global _db
  if _db is None:
    _db = mysql.connector.connect(**_config)
  return _db


def _close_db():
  global _db
  if _db is not None:
    _db.commit()
    _db.close()
  _db = None


def execute_query(query: str, params: list = None) -> list:
  db = _get_db()
  
  cursor = db.cursor(named_tuple=True)
  cursor.execute(query, params)
  data = cursor.fetchall()
  last_row_id = cursor.lastrowid
  
  cursor.close()
  _close_db()

  return (data, last_row_id)


