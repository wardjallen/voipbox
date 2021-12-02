docker exec backend aerich init -t src.database.config.TORTOISE_ORM
docker exec backend aerich init-db

docker exec backend aerich migrate

docker exec backend aerich upgrade


