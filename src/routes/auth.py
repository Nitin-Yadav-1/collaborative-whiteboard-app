
from fastapi import APIRouter
from schema.auth_schema import (
  LoginData, 
  RegisterData, 
  LoginResponse, 
  RegisterResponse
)


router = APIRouter()


@router.post("/login")
async def login(login_data: LoginData):
  token = 'secret-token'
  return LoginResponse(token=token)  


@router.post("/register")
async def register(register_data: RegisterData):
  pass