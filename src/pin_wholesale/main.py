# pin_wholesale/main.py
from fastapi import FastAPI


class PinWholesale(Base):
    __tablename__ = "pin_wholesale"

    id = Column(Integer, primary_key=True, index=True)
    vote = Column(String, index=True)
    forest_id = Column(Integer, ForeignKey("pin_forest.id"))

    forest = relationship("pinForest", back_populates="wholesale_votes")

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Wholesale model"}

@app.post("/")
async def handle_post(data: dict):
    return {"message": "Data received", "data": data}