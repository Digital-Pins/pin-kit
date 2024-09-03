# pin_PhiSNAIL/main.py
from fastapi import FastAPI


class PinPhiSNAIL(Base):
    __tablename__ = "pin_phisnail"

    id = Column(Integer, primary_key=True, index=True)
    vote = Column(String, index=True)
    forest_id = Column(Integer, ForeignKey("pin_forest.id"))

    forest = relationship("pinForest", back_populates="snail_votes")

app = FastAPI()





