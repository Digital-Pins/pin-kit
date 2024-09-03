from src.pin_database import init_db

def test_init_db():
    session = init_db()
    assert session is not None, "Session should be created"
    # يمكنك إجراء اختبارات إضافية هنا، مثل إضافة كائنات والتأكد من تخزينها في قاعدة البيانات
    session.close()
