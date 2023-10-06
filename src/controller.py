
from fastapi import WebSocket
import websocket_connection_manager as manager
import schema


async def handle_message(ws: WebSocket, msg: str) -> None:
  message = schema.create_message(msg)
  if message is None:
    return

  if message.msg_type == schema.MessageTypeEnum.ping:
    await manager.send_personal_message(ws, message.model_dump_json())
  elif message.msg_type == schema.MessageTypeEnum.broadcast_to_others:
    await manager.broadcast_to_others(ws, msg)
  elif message.msg_type == schema.MessageTypeEnum.save:
    pass
  elif message.msg_type == schema.MessageTypeEnum.load:
    pass

