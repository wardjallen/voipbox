from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from tortoise.contrib.fastapi import HTTPNotFoundError

import src.crud.users as crud
from src.auth.users import validate_user
from src.schemas.token import Status
from src.schemas.users import UserInSchema, UserOutSchema

from src.auth.jwthandler import (
    create_access_token,
    get_current_user,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)


router = APIRouter(
    prefix="/users", 
    tags=["Users"], 
    dependencies=[Depends(get_current_user)],
    responses={404: {"model": HTTPNotFoundError}}
    )





@router.get("/whoami", response_model=UserOutSchema)
async def read_users_me(current_user: UserOutSchema = Depends(get_current_user)):
    return current_user


@router.delete("/{user_id}", response_model=Status)
async def delete_user(
    user_id: int, current_user: UserOutSchema = Depends(get_current_user)
) -> Status:
    return await crud.delete_user(user_id, current_user)
