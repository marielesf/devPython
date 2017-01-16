import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative impor declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declaritive_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column (String(250), nullable=False)

class MenuItem(Base):
    __tablename__ =  'menu_item'
    name = Column(String(80), nullable = False)
    id = Column (Integer, primary_key = True)
    description = Column(String(250))
    price = Column(Strign(8))
    restaurant_id = Column(Integer ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
########insert at end of file##########

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
