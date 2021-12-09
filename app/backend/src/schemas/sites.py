from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Sites


SiteInSchema = pydantic_model_creator(
    Sites, name="SiteIn", exclude=["cluster_id"], exclude_readonly=True)
SiteOutSchema = pydantic_model_creator(
    Sites, name="Site", exclude =[
      "created_at", 
      "modified_at", 
      "cluster.clusterAxlUsername", 
      "cluster.clusterAxlPassword", 
      "cluster.created_at", 
      "cluster.modified_at"
    ]
)


class UpdateSite(BaseModel):
    siteName: Optional[str]

