
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

import websocket_connection_manager as manager
import controller
import routes.auth


app = FastAPI()
app.include_router(routes.auth.router)


@app.websocket("/ws")
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