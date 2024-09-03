from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from src.models import Base, PinForest, PinPhiSNAIL, PinPhiUSIIL, PinWholesale, PinSecurityHR, PinARCD, PinAIPowered, PinInventory, PinCustomerSupport, PinSales, PinMarketing, PinSupermarket, PinTechnicalSupport 


Base = declarative_base()

# إعداد قاعدة بيانات SQLite في الذاكرة
engine = create_engine('sqlite:///src/pin_database.db')  # هنا نستخدم ملف قاعدة بيانات فعلي بدلاً من قاعدة بيانات في الذاكرة
Base.metadata.create_all(engine)

# إنشاء جلسة
Session = sessionmaker(bind=engine)
session = Session()

# اختبار إنشاء كائنات من النماذج والتحقق من العلاقات
def test_create_models():
    # حذف أي سجلات موجودة بنفس الأسماء مسبقاً
    session.query(PinAIPowered).delete()
    session.query(PinCustomerSupport).delete()
    session.query(PinInventory).delete()
    session.query(PinSales).delete()
    session.query(PinMarketing).delete()
    session.query(PinSupermarket).delete()
    session.query(PinTechnicalSupport).delete()
    session.query(PinForest).delete()
    session.query(PinPhiSNAIL).delete()
    session.query(PinPhiUSIIL).delete()
    session.query(PinWholesale).delete()
    session.query(PinSecurityHR).delete()
    session.query(PinARCD).delete()
    session.commit()

    # إنشاء كائنات من النماذج
    ceo = PinForest(name="CEO Example")
    snail = PinPhiSNAIL(name="SNAIL Example", ceo=ceo)
    usiil = PinPhiUSIIL(name="USIIL Example", ceo=ceo)
    wholesale = PinWholesale(name="Wholesale Example", ceo=ceo)
    security_hr = PinSecurityHR(name="Security HR Example", ceo=ceo)
    arcd = PinARCD(name="ARCD Example", ceo=ceo)
    ai = PinAIPowered(name="AI Powered Example", ceo=ceo)
    customer_support = PinCustomerSupport(name="Customer Support Example", ceo=ceo)
    inventory = PinInventory(name="Inventory Example", ceo=ceo)
    sales = PinSales(name="Sales Example", ceo=ceo)
    marketing = PinMarketing(name="Marketing Example", ceo=ceo)
    supermarket = PinSupermarket(name="Supermarket Example", ceo=ceo)
    technical_support = PinTechnicalSupport(name="Technical Support Example", ceo=ceo)
    
    # إضافة الكائنات إلى الجلسة
    session.add_all([ceo, snail, usiil, wholesale, security_hr, arcd, ai, customer_support, inventory, marketing, sales, supermarket, technical_support])
    
    # حفظ التغييرات في قاعدة البيانات
    session.commit()
    
    # استرجاع الكائنات من قاعدة البيانات للتحقق من العلاقات
    retrieved_ceo = session.query(PinForest).filter_by(name="CEO Example").first()
    retrieved_pin_s = session.query(PinPhiSNAIL).filter_by(name="SNAIL Example").first()
    retrieved_pin_u = session.query(PinPhiUSIIL).filter_by(name="USIIL Example").first()
    retrieved_ai = session.query(PinAIPowered).filter_by(name="AI Powered Example").first()

    # طباعة النتائج للتحقق من العلاقات
    print(f"Retrieved CEO: {retrieved_ceo.name}")
    print(f"Retrieved pin_s: {retrieved_pin_s.name}, CEO: {retrieved_pin_s.ceo.name}")
    print(f"Retrieved pin_u: {retrieved_pin_u.name}, CEO: {retrieved_pin_u.ceo.name}")
    print(f"Retrieved AI Powered: {retrieved_ai.name}, CEO: {retrieved_ai.ceo.name}")
  

    assert ceo is not None, "CEO should be created"
    assert len(ceo.pin_s) == 1, "CEO should have one SNAIL"
    assert len(ceo.pin_u) == 1, "CEO should have one USIIL"
    assert len(ceo.wholesale) == 1, "CEO should have one Wholesale"
    assert len(ceo.security_hr) == 1, "CEO should have one Security HR"
    assert len(ceo.arcd) == 1, "CEO should have one ARCD"
    assert len(ceo.ai) == 1, "CEO should have one ai"
    assert len(ceo.customer_support) == 1, "CEO should have one Customer Support"
    assert len(ceo.inventory) == 1, "CEO should have one Inventory"
    assert len(ceo.marketing) == 1, "CEO should have one Marketing"
    assert len(ceo.sales) == 1, "CEO should have one Sales"
    assert len(ceo.supermarket) == 1, "CEO should have one Supermarket"
    assert len(ceo.technical_support) == 1, "CEO should have one Technical Support"
    
    
class MyModel(Base):
    __tablename__ = 'my_model'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
# اختبار تحديث الكائنات
def test_update_model():
    retrieved_snail = session.query(PinPhiSNAIL).filter_by(name="SNAIL Example").first()
    retrieved_snail.name = "Updated SNAIL"
    session.commit()
    updated_snail = session.query(PinPhiSNAIL).filter_by(name="Updated SNAIL").first()
    assert updated_snail is not None, "SNAIL should be updated"

# اختبار حذف الكائنات
def test_delete_model():
    retrieved_usiil = session.query(PinPhiUSIIL).filter_by(name="USIIL Example").first()
    session.delete(retrieved_usiil)
    session.commit()
    deleted_usiil = session.query(PinPhiUSIIL).filter_by(name="USIIL Example").first()
    assert deleted_usiil is None, "USIIL should be deleted"

# اختبار استثناءات
def test_exceptions():
    try:
        session.query(PinPhiSNAIL).filter_by(name="Non Existent").one()
    except Exception as e:
        assert isinstance(e, Exception), "Should raise an exception for non-existent entry"

# تنفيذ الاختبارات
test_create_models()
test_update_model()
test_delete_model()
test_exceptions()

# تنظيف الجلسة
session.close()
