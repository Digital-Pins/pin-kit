from sqlalchemy.orm import sessionmaker
from src.database import engine
from src.models import PinForest

# إنشاء جلسة
Session = sessionmaker(bind=engine)
session = Session()

# اختبار الاتصال بقاعدة البيانات عن طريق إنشاء كائن جديد وحفظه واسترجاعه
def test_database_connection():
    try:
        # إنشاء كائن جديد
        new_ceo = PinForest(name="Test CEO")
        
        # إضافته إلى الجلسة
        session.add(new_ceo)
        
        # حفظ التغييرات في قاعدة البيانات
        session.commit()
        
        # استرجاع الكائن للتحقق
        retrieved_ceo = session.query(PinForest).filter_by(name="Test CEO").first()
        
        # التحقق من نجاح العملية
        if retrieved_ceo:
            print(f"Successfully connected to the database and retrieved: {retrieved_ceo.name}")
        else:
            print("Failed to retrieve the object. Connection to the database might not be working properly.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # تنظيف الجلسة
        session.close()

# تنفيذ الاختبار
test_database_connection()
