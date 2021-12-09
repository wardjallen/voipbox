from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import DevicePools


DevicePoolInSchema = pydantic_model_creator(
    DevicePools, name="DevicePoolIn", exclude=["site_id"], exclude_readonly=True)
DevicePoolOutSchema = pydantic_model_creator(
    DevicePools, name="DevicePool", exclude =[
      "created_at", 
      "modified_at", 
    ]
)


