from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.sites as crud
from src.auth.jwthandler import get_current_user
from src.database.models import Clusters
from src.schemas.sites import SiteOutSchema, SiteInSchema, UpdateSite
from src.schemas.token import Status
from src.schemas.clusters import ClusterOutSchema


router = APIRouter(
    prefix="/sites", 
    tags=["Sites"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"model": HTTPNotFoundError}}
)


@router.get("/", response_model=List[SiteOutSchema],)
async def get_sites():
    return await crud.get_sites()


@router.get("/{site_id}", response_model=SiteOutSchema,)
async def get_site(site_id: int) -> SiteOutSchema:
    try:
        return await crud.get_site(site_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Site does not exist",
        )


@router.post("/", response_model=SiteOutSchema)
async def create_site(site: SiteInSchema, current_cluster: int) -> SiteOutSchema:
    cluster = await ClusterOutSchema.from_queryset_single(Clusters.get(id=current_cluster))
    return await crud.create_site(site, cluster)


@router.patch("/{site_id}", response_model=SiteOutSchema)
async def update_site(site_id: int, site: UpdateSite) -> SiteOutSchema:
    return await crud.update_site(site_id, site)


@router.delete("/{site_id}", response_model=Status)
async def delete_site(site_id: int):
    return await crud.delete_site(site_id)
