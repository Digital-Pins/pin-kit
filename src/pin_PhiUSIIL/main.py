# pin_PhiUSIIL/main.py
from fastapi import FastAPI


class PinPhiUSIIL(Base):
    __tablename__ = "pin_phiusiil"

    id = Column(Integer, primary_key=True, index=True)
    vote = Column(String, index=True)
    forest_id = Column(Integer, ForeignKey("pin_forest.id"))

    forest = relationship("pinForest", back_populates="usiil_votes")

app = FastAPI()


