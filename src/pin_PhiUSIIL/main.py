# pin_PhiUSIIL/main.py
from fastapi import FastAPI

app = FastAPI()


@app.post("/")
async def handle_post(data: dict):
    return {"message": "Data received", "data": data}
@app.get("/")
async def read_root():
    return {"message": "Welcome to the PhiUSIIL model"}