import pytest
from src.utils import model_names
from src.utils import validator


def test_model_names():
    assert model_names["pin_ai_powered"] == "ai"
    assert model_names["pin_arcd"] == "arcd"
    assert model_names["pin_customer_support"] == "customer support"
    assert model_names["pin_forest"] == "ceo"
    assert model_names["pin_inventory"] == "inventory"
    assert model_names["pin_marketing"] == "marketing"
    assert model_names["pin_PhiSNAIL"] == "pin_s"
    assert model_names["pin_PhiUSIIL"] == "pin_u"
    assert model_names["pin_sales"] == "sales"
    assert model_names["pin_security_hr"] == "security & hr"
    assert model_names["pin_supermarket"] == "supermarket"
    assert model_names["pin_technical_support"] == "technical support"
    assert model_names["pin_wholesale"] == "wholesale"



def test_validator():
    valid_data = {"name": "Test", "age": 30}
    schema = {"name": str, "age": int}
    assert validator(valid_data, schema) == True

    invalid_data = {"name": "Test", "age": "thirty"}
    try:
        validator(invalid_data, schema)
    except TypeError as e:
        assert str(e) == "Incorrect type for field age: expected int"


if __name__ == "__main__":
    pytest.main()
