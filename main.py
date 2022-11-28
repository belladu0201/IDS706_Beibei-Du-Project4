# pip install fastapi
# pip install "uvicorn[standard]"
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}