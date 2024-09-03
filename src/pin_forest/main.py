# pin_forest/main.py
from fastapi import FastAPI
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class PinForest(Base):
    __tablename__ = "pin_forest"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)

    usiil_votes = relationship("PinPhiUSIIL", back_populates="forest")
    wholesale_votes = relationship("PinWholesale", back_populates="forest")
    snail_votes = relationship("PinPhiSNAIL", back_populates="forest")
    
    
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Forest model"}

@app.post("/")
async def handle_post(data: dict):
    return {"message": "Data received", "data": data}