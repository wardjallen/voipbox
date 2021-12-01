import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

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





@app.get("/")
def home():
    return "Hello, World!"
