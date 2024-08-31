from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# نموذج للبيانات التي سيتم إرسالها واستقبالها
class InteractionData(BaseModel):
    key1: str
    key2: str

@app.get("/pin_forest")
def get_status():
    return {"status": "Pin_Forest API is running"}

# Endpoint للتفاعل مع نموذج Pin_PhiUSIIL
@app.post("/pin_forest/interact_with_pin_phiusiil")
def interact_with_pin_phiusiil(data: InteractionData):
    return {
        "message": "Interacted with Pin_PhiUSIIL successfully",
        "data": data.dict()
    }

# Endpoint للتفاعل مع نموذج Pin_PhiSNAIL
@app.post("/pin_forest/interact_with_pin_PhiSNAIL")
def interact_with_pin_PhiSNAIL(data: InteractionData):
    return {
        "message": "Interacted with Pin_PhiSNAIL successfully",
        "data": data.dict()
    }

# Endpoint للتفاعل مع نموذج pin_ai
@app.post("/pin_forest/interact_with_pin_ai")
def interact_with_pin_ai(data: InteractionData):
    return {
        "message": "Interacted with Pin_ai successfully",
        "data": data.dict()
    }

# Endpoint للتفاعل مع نموذج pin_arcd
@app.post("/pin_forest/interact_with_pin_arcd")
def interact_with_pin_arcd(data: InteractionData):
    return {
        "message": "Interacted with Pin_arcd successfully",
        "data": data.dict()
    }

# Endpoint للتفاعل مع نموذج pin_inventory
@app.post("/pin_forest/interact_with_pin_inventory")
def interact_with_pin_inventory(data: InteractionData):
    return {
        "message": "Interacted with Pin_inventory successfully",
        "data": data.dict()
    }

# Endpoint للتفاعل مع نموذج pin_marketing
@app.post("/pin_forest/interact_with_pin_marketing")
def interact_with_pin_marketing(data: InteractionData):
    return {
        "message": "Interacted with Pin_marketing successfully",
        "data": data.dict()
    }

# Endpoint للتفاعل مع نموذج pin_sales
@app.post("/pin_forest/interact_with_pin_sales")
def interact_with_pin_sales(data: InteractionData):
    return {
        "message": "Interacted with Pin_sales successfully",
        "data": data.dict()
    }

# Endpoint للتفاعل مع نموذج pin_security
@app.post("/pin_forest/interact_with_pin_security")
def interact_with_pin_security(data: InteractionData):
    return {
        "message": "Interacted with Pin_security successfully",
        "data": data.dict()
    }

# Endpoint للتفاعل مع نموذج pin_supermarket
@app.post("/pin_forest/interact_with_pin_supermarket")
def interact_with_pin_supermarket(data: InteractionData):
    return {
        "message": "Interacted with Pin_supermarket successfully",
        "data": data.dict()
    }

# Endpoint للتفاعل مع نموذج pin_customer_support
@app.post("/pin_forest/interact_with_pin_customer_support")
def interact_with_pin_customer_support(data: InteractionData):
    return {
        "message": "Interacted with Pin_customer_support successfully",
        "data": data.dict()
    }

# Endpoint للتفاعل مع نموذج pin_technical_support
@app.post("/pin_forest/interact_with_pin_technical_support")
def interact_with_pin_technical_support(data: InteractionData):
    return {
        "message": "Interacted with Pin_technical_support successfully",
        "data": data.dict()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5005)
