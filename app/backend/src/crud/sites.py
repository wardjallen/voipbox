from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Sites
from src.schemas.sites import SiteOutSchema
from src.schemas.token import Status


async def get_sites():
    return await SiteOutSchema.from_queryset(Sites.all())


async def get_site(site_id) -> SiteOutSchema:
    return await SiteOutSchema.from_queryset_single(Sites.get(id=site_id))


async def create_site(site, current_cluster) -> SiteOutSchema:
    print(site)
    site_dict = site.dict(exclude_unset=True)
    site_dict["cluster_id"] = current_cluster.id
    site_obj = await Sites.create(**site_dict)
    return await SiteOutSchema.from_tortoise_orm(site_obj)


async def update_site(site_id, site) -> SiteOutSchema:
    try:
        db_site = await SiteOutSchema.from_queryset_single(Sites.get(id=site_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Site {site_id} not found")

    await Sites.filter(id=site_id).update(**site.dict(exclude_unset=True))
    return await SiteOutSchema.from_queryset_single(Sites.get(id=site_id))



async def delete_site(site_id) -> Status:
    try:
        db_site = await SiteOutSchema.from_queryset_single(Sites.get(id=site_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Site {site_id} not found")

    deleted_count = await Sites.filter(id=site_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Site {site_id} not found")
    return Status(message=f"Deleted site {site_id}")

