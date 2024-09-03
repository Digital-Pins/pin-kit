# src/utils.py

# خريطة لأسماء النماذج المختصرة
model_names = {
    "pin_ai_powered": "ai",
    "pin_arcd": "arcd",
    "pin_customer_support": "customer support",
    "pin_forest": "ceo",
    "pin_inventory": "inventory",
    "pin_marketing": "marketing",
    "pin_PhiSNAIL": "pin_s",
    "pin_PhiUSIIL": "pin_u",
    "pin_sales": "sales",
    "pin_security_hr": "security & hr",
    "pin_supermarket": "supermarket",
    "pin_technical_support": "technical support",
    "pin_wholesale": "wholesale"
}

def get_model_name(key):
    """استرجاع الاسم المختصر للنموذج بناءً على المفتاح"""
    return model_names.get(key, key)

def validator(data, schema):
    """
    تحقق من صحة البيانات بناءً على المخطط المعطى.
    
    Args:
        data (dict): البيانات التي تحتاج إلى التحقق.
        schema (dict): المخطط الذي يحتوي على الحقول والأنواع المتوقعة.

    Returns:
        bool: True إذا كانت البيانات صحيحة.

    Raises:
        ValueError: إذا كان حقل مطلوب مفقودًا.
        TypeError: إذا كان نوع الحقل غير صحيح.
    """
    if not isinstance(data, dict):
        raise ValueError("Data must be a dictionary")
    
    for field, field_type in schema.items():
        if field not in data:
            raise ValueError(f"Missing required field: {field}")
        if not isinstance(data[field], field_type):
            raise TypeError(f"Incorrect type for field {field}: expected {field_type.__name__}")
    
    return True

# يمكنك إضافة وظائف أخرى إذا لزم الأمر
