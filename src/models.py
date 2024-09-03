from sqlalchemy import Column, Integer, String, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///pin_database.db')


Base = declarative_base()
Base.metadata.create_all(engine)
model_names = {
    "pin_ai_powered": "ai",
    "pin_arcd": "arcd",
    "pin_customer_support": "customer_support",
    "pin_forest": "ceo",
    "pin_inventory": "inventory",
    "pin_marketing": "marketing",
    "pin_PhiSNAIL": "pin_s",
    "pin_PhiUSIIL": "pin_u",
    "pin_sales": "sales",
    "pin_security_hr": "security_hr",
    "pin_supermarket": "supermarket",
    "pin_technical_support": "technical_support",
    "pin_wholesale": "wholesale"
}

class PinForest(Base):
    __tablename__ = model_names["pin_forest"]

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    # العلاقات مع النماذج الأخرى
    pin_s = relationship("PinPhiSNAIL", back_populates="ceo")
    pin_u = relationship("PinPhiUSIIL", back_populates="ceo")
    wholesale = relationship("PinWholesale", back_populates="ceo")
    security_hr = relationship("PinSecurityHR", back_populates="ceo")
    arcd = relationship("PinARCD", back_populates="ceo")
    ai = relationship("PinAIPowered", back_populates="ceo")
    customer_support = relationship("PinCustomerSupport", back_populates="ceo")
    inventory = relationship("PinInventory", back_populates="ceo")
    marketing = relationship("PinMarketing", back_populates="ceo")
    sales = relationship("PinSales", back_populates="ceo")
    supermarket = relationship("PinSupermarket", back_populates="ceo")
    technical_support = relationship("PinTechnicalSupport", back_populates="ceo")

class PinPhiSNAIL(Base):
    __tablename__ = model_names["pin_PhiSNAIL"]

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    
    ceo_id = Column(Integer, ForeignKey(f'{model_names["pin_forest"]}.id'))
    ceo = relationship("PinForest", back_populates="pin_s")

class PinPhiUSIIL(Base):
    __tablename__ = model_names["pin_PhiUSIIL"]

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    ceo_id = Column(Integer, ForeignKey(f'{model_names["pin_forest"]}.id'))
    ceo = relationship("PinForest", back_populates="pin_u")

class PinWholesale(Base):
    __tablename__ = model_names["pin_wholesale"]

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    ceo_id = Column(Integer, ForeignKey(f'{model_names["pin_forest"]}.id'))
    ceo = relationship("PinForest", back_populates="wholesale")

class PinSecurityHR(Base):
    __tablename__ = model_names["pin_security_hr"]

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    ceo_id = Column(Integer, ForeignKey(f'{model_names["pin_forest"]}.id'))
    ceo = relationship("PinForest", back_populates="security_hr")

class PinARCD(Base):
    __tablename__ = model_names["pin_arcd"]

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    ceo_id = Column(Integer, ForeignKey(f'{model_names["pin_forest"]}.id'))
    ceo = relationship("PinForest", back_populates="arcd")

class PinAIPowered(Base):
    __tablename__ = model_names["pin_ai_powered"]

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    ceo_id = Column(Integer, ForeignKey(f'{model_names["pin_forest"]}.id'))
    ceo = relationship("PinForest", back_populates="ai")

class PinCustomerSupport(Base):
    __tablename__ = model_names["pin_customer_support"]

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    ceo_id = Column(Integer, ForeignKey(f'{model_names["pin_forest"]}.id'))
    ceo = relationship("PinForest", back_populates="customer_support")

class PinInventory(Base):
    __tablename__ = model_names["pin_inventory"]

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    ceo_id = Column(Integer, ForeignKey(f'{model_names["pin_forest"]}.id'))
    ceo = relationship("PinForest", back_populates="inventory")

class PinMarketing(Base):
    __tablename__ = model_names["pin_marketing"]

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    ceo_id = Column(Integer, ForeignKey(f'{model_names["pin_forest"]}.id'))
    ceo = relationship("PinForest", back_populates="marketing")

class PinSales(Base):
    __tablename__ = model_names["pin_sales"]

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    ceo_id = Column(Integer, ForeignKey(f'{model_names["pin_forest"]}.id'))
    ceo = relationship("PinForest", back_populates="sales")

class PinSupermarket(Base):
    __tablename__ = model_names["pin_supermarket"]

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    ceo_id = Column(Integer, ForeignKey(f'{model_names["pin_forest"]}.id'))
    ceo = relationship("PinForest", back_populates="supermarket")

class PinTechnicalSupport(Base):
    __tablename__ = model_names["pin_technical_support"]

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    ceo_id = Column(Integer, ForeignKey(f'{model_names["pin_forest"]}.id'))
    ceo = relationship("PinForest", back_populates="technical_support")