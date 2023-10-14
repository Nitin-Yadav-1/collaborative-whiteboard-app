
from fastapi import FastAPI

from app.routers import auth, user, websocket


app = FastAPI()
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(websocket.router)