
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers import auth, user, websocket, whiteboard


app = FastAPI()
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(websocket.router)
app.include_router(whiteboard.router)


app.mount("/static", StaticFiles(directory="./app/static"), name="static")