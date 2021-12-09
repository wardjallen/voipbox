from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.clusters as crud
from src.auth.jwthandler import get_current_user
from src.schemas.clusters import ClusterOutSchema, ClusterInSchema, UpdateCluster
from src.schemas.token import Status


router = APIRouter(
    prefix="/clusters", 
    tags=["Clusters"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"model": HTTPNotFoundError}}
)


@router.get("/", response_model=List[ClusterOutSchema])
async def get_clusters():
    return await crud.get_clusters()


@router.get("/{cluster_id}", response_model=ClusterOutSchema)
async def get_cluster(cluster_id: int) -> ClusterOutSchema:
    try:
        return await crud.get_cluster(cluster_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Cluster does not exist",
        )


@router.post("/", response_model=ClusterOutSchema)
async def create_cluster(cluster: ClusterInSchema) -> ClusterOutSchema:
    return await crud.create_cluster(cluster)


@router.patch("/{cluster_id}", response_model=ClusterOutSchema)
async def update_cluster(
    cluster_id: int,
    cluster: UpdateCluster,
) -> ClusterOutSchema:
    return await crud.update_cluster(cluster_id, cluster)


@router.delete("/{cluster_id}", response_model=Status)
async def delete_cluster(cluster_id: int):
    return await crud.delete_cluster(cluster_id)
