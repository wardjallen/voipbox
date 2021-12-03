import typing


from typing import Optional
from pydantic import BaseModel

from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Clusters

ClusterInSchema = pydantic_model_creator(
    Clusters, name="ClusterIn", exclude_readonly=True
)
ClusterOutSchema = pydantic_model_creator(
    Clusters, name="ClusterOut", exclude=["clusterAxlPassword", "created_at", "modified_at"]
)


class UpdateCluster(BaseModel):
    clusterName: Optional[str]
    clusterAxlUsername: Optional[str]
    clusterAxlPassword: Optional[str]