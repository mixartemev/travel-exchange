from sqlalchemy import func
from models import *


class Record(Base):
    __tablename__ = 'records'
    stamp = Column(DateTime, primary_key=True, default=func.now())
    winner_id = Column(String, ForeignKey('tours.identity'))
    type_id = Column(SmallInteger)

    winner = relationship("Tour", back_populates="win")

    def __init__(
            self,
            stamp,
            winner_id: str,
            type_id: int,
    ):
        self.stamp = stamp
        self.winner_id = winner_id
        self.type_id = type_id
