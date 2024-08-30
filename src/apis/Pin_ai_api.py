from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# نقطة البداية
@app.get("/pin_ai")
def get_status():
    return {"status": "pin_ai API is running"}

# تعريف نموذج البيانات الذي سنستقبله
class InteractionData(BaseModel):
    message: str

# Endpoint للتفاعل مع نموذج pin_PhiUSIIL
@app.post("/pin_ai/interact_with_pin_PhiUSIIL")
def interact_with_pin_PhiUSIIL(data: InteractionData):
    # تنفيذ المنطق المطلوب للتفاعل مع pin_PhiUSIIL
    response = {
        "message": "Interacted with pin_PhiUSIIL successfully",
        "data": data
    }
    return response

# Endpoint للتفاعل مع نموذج pin_arcd
@app.post("/pin_ai/interact_with_pin_arcd")
def interact_with_pin_arcd(data: InteractionData):
    # تنفيذ المنطق المطلوب للتفاعل مع pin_arcd
    response = {
        "message": "Interacted with pin_arcd successfully",
        "data": data
    }
    return response
