
from enum import Enum
import json
import pydantic


class MessageTypeEnum(str, Enum):
  ping = "ping"
  broadcast_to_others = "broadcast_to_others"
  save = "save"
  load = "load"
  invalid = "invalid"


class Message(pydantic.BaseModel):
  action: str
  data: str
  msg_type: MessageTypeEnum = MessageTypeEnum.invalid

  @pydantic.model_validator(mode='after')
  @classmethod
  def set_message_type(cls, msg):
    '''
    Sets the type of message based on 'action' and 'data' properties.
    '''
    if msg.action == 'ping' and msg.data == '':
      msg.msg_type = MessageTypeEnum.ping
    elif msg.action == 'broadcast_to_others':
      msg.msg_type = MessageTypeEnum.broadcast_to_others
    elif msg.action == 'save':
      msg.msg_type = MessageTypeEnum.save
    elif msg.action == 'load' and msg.data == '':
      msg.msg_type = MessageTypeEnum.load


def create_message(json_data: str) -> Message | None:
  '''
  Try to convert a json string to Message object. Returns None if fails.
  '''
  try:
    dict_data = json.loads(json_data)
    msg = Message(**dict_data)
  except pydantic.ValidationError:
    msg = None
  except json.JSONDecodeError:
    msg = None

  return msg