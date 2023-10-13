
from fastapi import FastAPI

from .http_app import router as http_router
from .websocket_app import router as websocket_router


app = FastAPI()
app.include_router(http_router)
app.include_router(websocket_router)