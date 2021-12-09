from os import device_encoding
from re import S
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.devicepools as crud
from src.auth.jwthandler import get_current_user
from src.database.models import Sites
from src.schemas.devicepools import DevicePoolInSchema, DevicePoolOutSchema
from src.schemas.token import Status
from src.schemas.sites import SiteOutSchema

from src.cucm.cucm import ucm

ucm.get_device_pools()

router = APIRouter(
    prefix="/cucm", 
    tags=["CUCM"],
    dependencies=[Depends(get_current_user)],
    #responses={404: {"model": HTTPNotFoundError}}
)

@router.get("/system/device_pools")
def list_device_pools():
    return ucm.get_device_pools()

@router.get("/call_routing/partions")
def list_partions():
    return ucm.get_partitions()

@router.get("/call_routing/calling_search_spaces")
def list_calling_search_spaces():
    return ucm.get_calling_search_spaces()



