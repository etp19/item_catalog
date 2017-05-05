# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from pkg import app
from pkg.auth.models import User, Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship



class Restaurant(Base):
    __tablename__ = 'restaurant'

    name = Column(String(80), nullable = False)
    phone = Column(String(80), nullable=False)
    email = Column(String(250))
    website = Column(String(300))
    food_type = Column(String(80), nullable=False)
    description = Column(String(300), nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'phone': self.phone,
            'email': self.email,
            'website': self.website,
            'description': self.description,
        }

    @staticmethod
    def user_creator(user, restaurant_id):
        test_user = app.db_session.query(Restaurant).filter_by(id=restaurant_id).first()
        if test_user.user_id == user:
            return True
        else:
            return False


class RestaurantAddress(Base):
    __tablename__ = 'restaurant_address'

    street = Column(String(250), nullable=False)
    city = Column(String(80), nullable=False)
    state = Column(String(80), nullable=False)
    zip_code = Column(String(300), nullable=False)
    id = Column(Integer, primary_key = True)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'street': self.street,
            'city': self.city,
            'state': self.state,
            'zip code': self.zip_code,
        }
