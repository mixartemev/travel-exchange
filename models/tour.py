from sqlalchemy.orm import backref
from models import *
from datetime import datetime

operators = {
    40: 'Pegas Touristic',
}


class Tour(Base):
    __tablename__ = 'tours'
    id = Column(Integer, primary_key=True)
    identity = Column(String, unique=True)
    price = Column(Integer)
    oilTax = Column(Integer)
    originalPrice = Column(Integer)
    nights = Column(SmallInteger)
    group = Column(SmallInteger)
    meal = Column(SmallInteger)
    # meal = Column(Enum('RO', 'BB', 'HB', 'FB', 'AI', 'UAI'))
    checkin = Column(Date)
    hotel_id = Column(Integer, ForeignKey('hotels.id'))
    operator_id = Column(SmallInteger)
    room = Column(Enum('ROH'))
    available = Column(Boolean)
    less = Column(Boolean)
    rate = Column(DECIMAL(7, 6))
    offers = relationship("Offer", back_populates="bc")
    mcityOffers = relationship("McityOffer", back_populates="bc")
    # children = relationship("Bc", back_populates="parent")
    # parent = relationship("Bc", remote_side=[id],  back_populates="children")
    children = relationship("Bc", backref=backref('parent', remote_side=[id]))

    def __init__(self, id: int, typ: str, name: str, parent_id, address: str, editDate):
        self.id = id
        self.typ = typ
        self.name = name
        self.parent_id = parent_id if parent_id else None
        self.address = address
        self.editDate = datetime.strptime(editDate, "%d.%m.%Y").date()
