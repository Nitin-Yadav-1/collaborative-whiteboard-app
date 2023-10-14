
from app.models import user_model
from app.services import password

# fill test users =============================================================
test_users = [
  {"email": "test@gmail.com", "password": "password"},
  {"email": "sample@gmail.com", "password": "password"},
  {"email": "testing@gmail.com", "password": "password"},
]
for user in test_users:
  user['password'] = password.generate_hashed_password(user['password'])
  user = user_model.create_user(**user)
  print(f"User created => {user}")

