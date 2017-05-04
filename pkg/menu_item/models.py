# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from pkg.auth.models import Base, User
from pkg.restaurant.models import Restaurant
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }
