from enum import unique
from tortoise import fields, models

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
