from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Clusters
from src.schemas.clusters import ClusterOutSchema
from src.schemas.token import Status


async def get_clusters():
    return await ClusterOutSchema.from_queryset(Clusters.all())


async def get_cluster(cluster_id) -> ClusterOutSchema:
    return await ClusterOutSchema.from_queryset_single(Clusters.get(id=cluster_id))


async def create_cluster(cluster) -> ClusterOutSchema:
    cluster_dict = cluster.dict(exclude_unset=True)
    cluster_obj = await Clusters.create(**cluster_dict)
    return await ClusterOutSchema.from_tortoise_orm(cluster_obj)


async def update_cluster(cluster_id, cluster) -> ClusterOutSchema:
    try:
        await ClusterOutSchema.from_queryset_single(Clusters.get(id=cluster_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Cluster {cluster_id} not found")

    await Clusters.filter(id=cluster_id).update(**cluster.dict(exclude_unset=True))
    return await ClusterOutSchema.from_queryset_single(Clusters.get(id=cluster_id))


async def delete_cluster(cluster_id) -> Status:
    try:
        await ClusterOutSchema.from_queryset_single(Clusters.get(id=cluster_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Cluster {cluster_id} not found")

    deleted_count = await Clusters.filter(id=cluster_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Cluster {cluster_id} not found")
    return Status(message=f"Deleted cluster {cluster_id}")

