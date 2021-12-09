from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import DevicePools
from src.schemas.devicepools import DevicePoolOutSchema
from src.schemas.token import Status


async def get_devicepools():
    return await DevicePoolOutSchema.from_queryset(DevicePools.all())


async def get_devicepool(devicepool_id) -> DevicePoolOutSchema:
    return await DevicePoolOutSchema.from_queryset_single(DevicePools.get(id=devicepool_id))


async def create_devicepool(devicepool, current_site) -> DevicePoolOutSchema:
    devicepool_dict = devicepool
    devicepool_dict["site_id"] = current_site.id
    devicepool_obj = await DevicePools.create(**devicepool_dict)
    return await DevicePoolOutSchema.from_tortoise_orm(devicepool_obj)


