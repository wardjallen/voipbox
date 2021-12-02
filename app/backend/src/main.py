import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM

from src.routes import users


app = FastAPI()

Tortoise.init_models(["src.database.models"], "models")


ALLOWED_ORIGINS = [
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=True)



@app.get("/")
def home():
    return "Hello, World!"
