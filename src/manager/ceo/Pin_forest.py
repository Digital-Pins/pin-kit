from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import sys
sys.path.append('/mnt/c/Users/Digital-PIN/Documents/pin-kit/src')

app = FastAPI()

# نقطة البداية
@app.get("/pin_forest")
async def get_status():
    return {"status": "Pin_Forest API is running"}

# تعريف نموذج البيانات للتفاعل
class InteractionData(BaseModel):
    key1: str
    key2: str

# Endpoint للتفاعل مع نموذج Pin_PhiUSIIL
@app.post("/pin_forest/interact_with_pin_phiusiil")
async def interact_with_pin_phiusiil(data: InteractionData):
    # تنفيذ المنطق المطلوب للتفاعل مع Pin_PhiUSIIL
    response = {
        "message": "Interacted with Pin_PhiUSIIL successfully",
        "data": data.dict()
    }
    return response

# Endpoint للتفاعل مع نموذج Pin_PhiSNAIL
@app.post("/pin_forest/interact_with_pin_phisnail")
async def interact_with_pin_phisnail(data: InteractionData):
    # تنفيذ المنطق المطلوب للتفاعل مع Pin_PhiSNAIL
    response = {
        "message": "Interacted with Pin_PhiSNAIL successfully",
        "data": data.dict()
    }
    return response

# المزيد من نقاط النهاية (endpoints) للتفاعل مع النماذج الأخرى
