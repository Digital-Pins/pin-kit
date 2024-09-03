# src/pin_ai_powered/main.py
from fastapi import FastAPI, APIRouter
from src.pin_ai_powered.process import process_data_function
from src.utils import validate_data

# إنشاء تطبيق FastAPI
app = FastAPI()

# إنشاء APIRouter
router = APIRouter()

# تعريف المسارات باستخدام التطبيق الرئيسي
@app.get("/")
async def read_root():
    return {"message": "Welcome to the AI-Powered model"}

@app.post("/")
async def handle_post(data: dict):
    return {"message": "Data received", "data": data}

# تعريف مسار في APIRouter
@router.post("/process")
async def process_data(data: dict):
    validate_data(data)  # استخدام الوظيفة المشتركة
    return {"message": "Data processed", "data": data}

@router.post("/process")
async def process_data(data: dict):
    return process_data_function(data)

# ربط APIRouter بالتطبيق الرئيسي
app.include_router(router)



