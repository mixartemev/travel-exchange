from models import *

operators = {
    40: 'Pegas Touristic',
}


class Tour(Base):
    __tablename__ = 'tours'
    identity = Column(String, primary_key=True)
    price = Column(Integer)
    oil_tax = Column(Integer)
    original_price = Column(Integer)
    nights = Column(SmallInteger)
    group = Column(SmallInteger)
    meal = Column(SmallInteger)
    # meal = Column(Enum('RO', 'BB', 'HB', 'FB', 'AI', 'UAI'))
    checkin = Column(Date)
    hotel_id = Column(Integer, ForeignKey('hotels.idd'))
    operator_id = Column(SmallInteger)
    room = Column(String)
    hotel_available = Column(SmallInteger)
    less = Column(Boolean)
    rate = Column(DECIMAL(7, 6))

    hotel = relationship("Hotel", back_populates="offers")

    def __init__(
            self,
            identity: str,
            price: int,
            oil_tax: int,
            original_price: int,
            nights: int,
            group: int,
            meal: int,
            checkin,
            hotel_id: int,
            operator_id: int,
            room: str,
            hotel_available: int,
            less: bool,
            rate: float
    ):
        self.identity = identity
        self.price = price
        self.oil_tax = oil_tax
        self.original_price = original_price
        self.nights = nights
        self.group = group
        self.meal = meal
        self.checkin = checkin
        self.hotel_id = hotel_id
        self.operator_id = operator_id
        self.room = room
        self.hotel_available = hotel_available
        self.less = less
        self.rate = rate
