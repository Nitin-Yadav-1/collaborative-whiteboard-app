
from app.models import db
from app.schema.whiteboard_schema import Whiteboard


def get_whiteboards_owned(user_id: int) -> list[Whiteboard]:
  query = f'''SELECT DISTINCT * FROM whiteboard WHERE owner_id={user_id}'''
  data = db.execute_query(query)
  whiteboards = []
  for row in data:
    board = Whiteboard(**row._asdict())
    whiteboards.append(board)
  return whiteboards


def get_whiteboards_shared(user_id: int) -> list[Whiteboard]:
  query = f'''
    SELECT DISTINCT * 
    FROM whiteboard 
    WHERE id
    IN (
      SELECT DISTINCT whiteboard_id 
      FROM shared 
      WHERE user_id={user_id}
    );
  '''
  data = db.execute_query(query)
  whiteboards = []
  for row in data:
    board = Whiteboard(**row._asdict())
    whiteboards.append(board)
  return whiteboards


def get_whiteboards(user_id: int) -> list[Whiteboard]:
  owned = get_whiteboards_owned(user_id)
  shared = get_whiteboards_shared(user_id)
  return owned + shared


def get_shared_emails(whiteboard_id: int) -> list[str]:
  query=f'''
    SELECT email 
    FROM user 
    WHERE id 
    IN (
      SELECT user_id 
      FROM shared 
      WHERE whiteboard_id={whiteboard_id}
    );
  '''
  data = db.execute_query(query)
  emails = [ row.email for row in data]
  return emails