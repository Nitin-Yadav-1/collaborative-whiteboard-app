
from fastapi import APIRouter, HTTPException, status

from app.schema.auth_schema import (
  LoginData, 
  RegisterData, 
  LoginResponse, 
  RegisterResponse
)
from app.models import user_model
from app.services import password, tkn


router = APIRouter(tags=['Authentication'])


@router.post("/login")
async def login(login_data: LoginData) -> LoginResponse:
  user = user_model.get_user_by_email(login_data.email)
  if user is None:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail='Invalid Credentials'
    )

  if not password.validate(login_data.password, user.password):
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail='Invalid Credentials'
    )

  token = tkn.create_token(user.id)
  return LoginResponse(token=token)  


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(register_data: RegisterData) -> RegisterResponse:
  user = user_model.get_user_by_email(register_data.email)
  if user is not None:
    raise HTTPException(
      status_code=status.HTTP_409_CONFLICT,
      detail="A user with this email already exists."
    )

  user = user_model.create_user(
    email=register_data.email, 
    password=password.generate_hashed_password(register_data.password)
  )

  token = tkn.create_token(user.id)
  return RegisterResponse(token=token)
