
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from . import controller
from . import websocket_connection_manager as manager


router = APIRouter(tags=['WebSocket'])
  

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
  '''
  Establish websocket connection and send/receive messages.
  '''
  await manager.connect(websocket)
  try:
    while True:
      data = await websocket.receive_text()
      await controller.handle_message(websocket, data)
  except WebSocketDisconnect:
    await manager.disconnect(websocket)


__all__ = ["router"]