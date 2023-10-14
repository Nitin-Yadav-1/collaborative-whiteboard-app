

import mysql.connector

config = {
  "host" : "localhost",
  "user" : "python-app",
  "password" : "python-app",
  "database" : "collaborative_whiteboard"
}

conn = mysql.connector.connect(**config)


def execute_query(query: str) -> None:
  conn.reconnect()
  cursor = conn.cursor()
  try:
    cursor.execute(query)
  except Exception as e:
    print(e)
  finally:
    cursor.close()


# delete 'previous' tables ====================================================
execute_query('''DROP TABLE IF EXISTS shared;''')
execute_query('''DROP TABLE IF EXISTS whiteboard;''')
execute_query('''DROP TABLE IF EXISTS user;''')


# Create 'user' table =========================================================
create_user_query = '''
CREATE TABLE user(
  id INT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(400) NOT NULL UNIQUE,
  password VARCHAR(100) NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

'''
execute_query(create_user_query)
print("'user' table created")


# create 'whiteboard' table ===================================================
create_whiteboard_query = '''
CREATE TABLE whiteboard(
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(50) NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_modified DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  thumbnail_image VARCHAR(50),
  data TEXT,
  owner_id INT NOT NULL,
  FOREIGN KEY(owner_id) REFERENCES user(id) ON DELETE CASCADE
);
'''
execute_query(create_whiteboard_query)
print("'whiteboard' table created")


# create 'shared' table =======================================================
create_shared_query = '''
CREATE TABLE shared(
  user_id INT NOT NULL,
  whiteboard_id INT NOT NULL,
  FOREIGN KEY(user_id) REFERENCES user(id) ON DELETE CASCADE,
  FOREIGN KEY(whiteboard_id) REFERENCES whiteboard(id) ON DELETE CASCADE
);
'''
execute_query(create_shared_query)
print("'shared' table created")

conn.close()