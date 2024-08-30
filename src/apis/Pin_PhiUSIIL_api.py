from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    key1: str
    key2: str

@app.get("/Pin_PhiUSIIL")
async def get_status():
    return {"status": "Pin_PhiUSIIL API is running"}

@app.post("/Pin_PhiUSIIL/interact_with_pin_forest")
async def interact_with_pin_forest(data: Data):
    # تنفيذ المنطق المطلوب للتفاعل مع Pin_Forest
    response = {
        "message": "Interacted with Pin_Forest successfully",
        "data": data.dict()
    }
    return response

@app.post("/pin_PhiUSIIL/interact_with_pin_PhiSNAIL")
async def interact_with_Pin_PhiSNAIL(data: Data):
    # تنفيذ المنطق المطلوب للتفاعل مع Pin_PhiSNAIL
    response = {
        "message": "Interacted with Pin_PhiSNAIL successfully",
        "data": data.dict()
    }
    return response
