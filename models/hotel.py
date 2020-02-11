from models import *


class Hotel(Base):
    __tablename__ = 'hotels'
    idd = Column(Integer, primary_key=True)
    name = Column(String)  # , unique=True)
    resort = Column(SmallInteger)
    country = Column(SmallInteger)
    category = Column(SmallInteger)
    rating = Column(DECIMAL(7, 6))
    airport = Column(SmallInteger)
    beach = Column(SmallInteger)
    beach_line = Column(SmallInteger)
    beach_owner = Column(Boolean)
    popular = Column(Boolean)
    children = Column(Boolean)

    offers = relationship("Tour", back_populates="hotel")

    def __init__(
            self,
            idd: int,
            name: str,
            resort: int,
            country: int,
            category: int,
            rating: float,
            airport: int,
            beach: int,
            beach_line: int,
            beach_owner: bool,
            popular: bool,
            children: bool,
    ):
        self.idd = idd
        self.name = name
        self.resort = resort
        self.country = country
        self.category = category
        self.rating = rating
        self.airport = airport
        self.beach = beach
        self.beach_line = beach_line
        self.beach_owner = beach_owner
        self.popular = popular
        self.children = children

    def link(self):
        return 'https://travelata.ru/goto/hotel/{}'.format(self.idd)
