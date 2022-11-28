# pip install fastapi
# pip install "uvicorn[standard]"
import os
import json
from fastapi import FastAPI
import uvicorn
from mylib.runhealth import health_generator
import statistics

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello IDS706! This is a Repo for IDS706 Project 4!"}

@app.get("/health/{health}")
async def healthstatus(df: dataframe):
    """Adds a fruit to random fruit"""

    chosen_random_ten = health_generator(df)
    output = statistics.mode(set(chosen_random_ten))
    return {"mode_health_status": chosen_random_ten}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
