
from app.models import db, user_model
from app.schema.whiteboard_schema import (
  Whiteboard, 
  WhiteboardInfo, 
  WhiteboardCreate
)


def get_whiteboard_by_id(whiteboard_id: int) -> Whiteboard | None:
  query = f'''SELECT * FROM whiteboard WHERE id=%s'''
  params = (whiteboard_id,)
  data, _ = db.execute_query(query, params)
  if len(data) == 0:
    return None
  return Whiteboard(**data[0]._asdict())  


def get_whiteboards(user_id: int) -> list[Whiteboard]:
  query = f'''
    SELECT * 
    FROM whiteboard
    WHERE 
      id IN
        (SELECT whiteboard_id FROM shared WHERE user_id=%s)
  '''
  params = (user_id,)
  data, _ = db.execute_query(query, params)
  boards = [Whiteboard(**row._asdict()) for row in data]
  return boards


def get_shared_emails(whiteboard_id: int) -> list[str]:
  query=f'''
    SELECT email 
    FROM user 
    WHERE id 
    IN (
      SELECT user_id 
      FROM shared 
      WHERE whiteboard_id=%s
    )
  '''
  params = (whiteboard_id,)
  data, _ = db.execute_query(query, params)
  emails = [row.email for row in data]
  return emails


def create_whiteboard(whiteboard: WhiteboardCreate, user_id: int) -> Whiteboard:
  query=f'''
    INSERT INTO whiteboard 
      (title, owner_id) 
    VALUES 
      (%s, %s)
  '''
  params = [whiteboard.title, user_id]
  data, whiteboard_id = db.execute_query(query, params)
  
  user = user_model.get_user_by_id(user_id)
  whiteboard.share_with.append(user.email)
  share_whiteboard_with(whiteboard_id, set(whiteboard.share_with))
  
  return get_whiteboard_by_id(whiteboard_id)


def share_whiteboard_with(whiteboard_id: int, share_with: set[str]) -> None:
  query = f'''
    INSERT INTO 
      shared (user_id, whiteboard_id)
    VALUES
      (%s, %s)
  '''
  for email in share_with:
    user = user_model.get_user_by_email(email)
    if user is None:
      continue
    params = (user.id, whiteboard_id)
    db.execute_query(query, params)