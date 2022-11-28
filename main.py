# pip install fastapi
# pip install "uvicorn[standard]"
import os
import json
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello IDS706! This is a Repo for IDS706 Project 4!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}