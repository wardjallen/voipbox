from enum import unique
from tortoise import fields, models, Tortoise

class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, unique=True)
    full_name = fields.CharField(max_length=64, null=True)
    password = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

class Clusters(models.Model):
    id = fields.IntField(pk=True)
    clusterName = fields.CharField(max_length=64, unique=True)
    clusterAxlUsername = fields.CharField(max_length=255, null=True)
    clusterAxlPassword = fields.CharField(max_length=255, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

class Sites(models.Model):
    id = fields.IntField(pk=True)
    siteName = fields.CharField(max_length=32, unique=True)
    cluster = fields.ForeignKeyField("models.Clusters", related_name="sites")
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.siteName}, {self.cluster_id} on {self.created_at}"

class DevicePools(models.Model):
    id = fields.IntField(pk=True)
    devicePoolName = fields.CharField(max_length=32, unique=True)
    site = fields.ForeignKeyField("models.Sites", related_name="device_pools")
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.devicePoolName}, {self.site_id} on {self.created_at}"


Tortoise.init_models(["src.database.models"], "models")

