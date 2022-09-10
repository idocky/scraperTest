from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float

from db import Base


class Ads(Base):
    __tablename__ = 'ads'

    id = Column(Integer, primary_key=True)
    picture = Column('picture', String)
    title = Column('title', String)
    date = Column('date', Date)
    city = Column('city', String)
    beds = Column('beds', String)
    content = Column('content', String)
    price = Column('price', Float)
    currency = Column('currency', String)



