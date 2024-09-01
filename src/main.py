from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# استيراد النماذج
from src.pin_ai_powered.main import app as pin_ai_powered_app
from src.pin_arcd.main import app as pin_arcd_app
from src.pin_customer_support.main import app as pin_customer_support_app
from src.pin_forest.main import app as pin_forest_app
from src.pin_inventory.main import app as pin_inventory_app
from src.pin_marketing.main import app as pin_marketing_app
from src.pin_PhiSNAIL.main import app as pin_PhiSNAIL_app
from src.pin_PhiUSIIL.main import app as pin_PhiUSIIL_app
from src.pin_sales.main import app as pin_sales_app
from src.pin_security_hr.main import app as pin_security_hr_app
from src.pin_supermarket.main import app as pin_supermarket_app
from src.pin_technical_support.main import app as pin_technical_support_app
from src.pin_wholesale.main import app as pin_wholesale_app

# إنشاء تطبيق FastAPI الرئيسي
app = FastAPI()

# إعداد CORS إذا لزم الأمر
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # يمكنك تخصيص هذا
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# توجيه الطلبات إلى النماذج المختلفة
app.mount("/pin_ai_powered", pin_ai_powered_app)
app.mount("/pin_arcd", pin_arcd_app)
app.mount("/pin_customer_support", pin_customer_support_app)
app.mount("/pin_forest", pin_forest_app)
app.mount("/pin_inventory", pin_inventory_app)
app.mount("/pin_marketing", pin_marketing_app)
app.mount("/pin_PhiSNAIL", pin_PhiSNAIL_app)
app.mount("/pin_PhiUSIIL", pin_PhiUSIIL_app)
app.mount("/pin_sales", pin_sales_app)
app.mount("/pin_security_hr", pin_security_hr_app)
app.mount("/pin_supermarket", pin_supermarket_app)
app.mount("/pin_technical_support", pin_technical_support_app)
app.mount("/pin_wholesale", pin_wholesale_app)

@app.get("/")
async def root():
    return {"message": "Main API is running"}

# مثال على مسار يدعم POST
@app.post("/process")
async def process_data(data: dict):
    return {"message": "Data processed", "data": data}
# نقطة الدخول لتشغيل التطبيق
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)