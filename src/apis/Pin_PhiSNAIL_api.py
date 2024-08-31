from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    key1: str
    key2: str

@app.get("/pin_PhiSNAIL")
async def get_status():
    return {"status": "Pin_PhiSNAIL API is running"}

@app.post("/pin_PhiSNAIL/interact_with_pin_forest")
async def interact_with_pin_forest(data: Data):
    # تنفيذ المنطق المطلوب للتفاعل مع Pin_Forest
    response = {
        "message": "Interacted with Pin_Forest successfully",
        "data": data.dict()
    }
    return response

@app.post("/pin_PhiSNAIL/interact_with_pin_PhiUSIIL")
async def interact_with_pin_PhiUSIIL(data: Data):
    # تنفيذ المنطق المطلوب للتفاعل مع Pin_PhiUSIIL
    response = {
        "message": "Interacted with Pin_PhiUSIIL successfully",
        "data": data.dict()
    }
    return response
