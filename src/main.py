import logging
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from src.database import init_db, Base  # التأكد من استيراد Base بشكل صحيح
from src.utils import model_names, validator  # استخدام utils للوظائف المساعدة



# استيراد التطبيقات المرتبطة بالنماذج
from src.pin_ai_powered.main import app as ai_powered_app
from src.pin_forest.main import app as pin_forest_app
# إضافة المزيد من الاستيرادات حسب الحاجة للنماذج الأخرى

app = FastAPI()

logging.basicConfig(level=logging.INFO)

# تهيئة قاعدة البيانات
init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://your-allowed-origin.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount routes for each model
for model_key, model_name in model_names.items():
    try:
        app.mount(f"/{model_name}", globals()[f"pin_{model_key}_app"])
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Model {model_key} not found.")

@app.get("/")
async def root():
    return {"message": "Main API is running"}

@app.post("/process")
async def process_data(data: dict):
    try:
        # استخدام الدالة المخصصة للتحقق من صحة البيانات
        validator(data, {"data": str})  # تحديد المفتاح "data" ونوعه
        return {"message": "Data processed", "data": data["data"]}
    except Exception as e:
        logging.error(f"خطأ في معالجة البيانات: {e}")
        raise HTTPException(status_code=400, detail="Error processing data")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
