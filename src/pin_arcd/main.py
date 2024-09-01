# pin_arcd/main.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Welcome to the ARCD model"}

@app.post("/")
async def handle_post(data: dict):
    return {"message": "Data received", "data": data}