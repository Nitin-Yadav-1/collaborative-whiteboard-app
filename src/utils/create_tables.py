

import mysql.connector

config = {
  "host" : "localhost",
  "user" : "python-app",
  "password" : "python-app",
  "database" : "collaborative_whiteboard"
}

conn = mysql.connector.connect(**config)

def execute_query(query: str) -> None:
  cursor = conn.cursor()
  try:
    cursor.execute(create_user_query)
    print("'user' table created")
  except Exception as e:
    print("error occured while creating 'user' table")
    print(e)
  finally:
    cursor.close()


# Create 'user' table
create_user_query = '''

DROP TABLE IF EXISTS user;

CREATE TABLE user(
  id INT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(400) NOT NULL UNIQUE,
  password VARCHAR(100) NOT NULL,
  created_at DATETIME NOT NULL DEFAULT NOW()
);

'''
execute_query(create_user_query)


# create 'whiteboard' table


# create 'shared' table


conn.close()