from pkg.mod_auth.models import Base
from pkg.mod_auth.models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pkg.menu_item.models import MenuItem
from pkg.restaurant.models import Restaurant, RestaurantAddress

engine = create_engine('sqlite:///restaurants.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# session.query(User).delete()
# session.query(Restaurant).delete()
# session.query(MenuItem).delete()
# session.close()
# Base.metadata.drop_all(bind=engine)


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Menu for UrbanBurger
restaurant1 = Restaurant(user_id=1, name="Urban Burger", phone="1111112222", email="test@test.com", food_type="mix",
                         website="www.test.com", description="test")

session.add(restaurant1)
session.commit()

restaurantaddres = RestaurantAddress(restaurant_id=1, street="1 road", city="lansing",
                                     state="Michigan", zip_code="48910")

session.add(restaurantaddres)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Veggie Burger",
                     description="Juicy grilled veggie patty with tomato mayo and lettuce", price="$7.50",
                     course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem1 = MenuItem(user_id=1, name="French Fries", description="with garlic and parmesan", price="$2.99",
                     course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Chicken Burger",
                     description="Juicy grilled chicken patty with tomato mayo and lettuce", price="$5.50",
                     course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Chocolate Cake", description="fresh baked and served with ice cream",
                     price="$3.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Sirloin Burger", description="Made with grade A beef", price="$7.99",
                     course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Root Beer", description="16oz of refreshing goodness", price="$1.99",
                     course="Beverage", restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Iced Tea", description="with Lemon", price="$.99", course="Beverage",
                     restaurant=restaurant1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="Grilled Cheese Sandwich", description="On texas toast with American Cheese",
                     price="$3.49", course="Entree", restaurant=restaurant1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="Veggie Burger",
                     description="Made with freshest of ingredients and home grown spices", price="$5.99",
                     course="Entree", restaurant=restaurant1)

session.add(menuItem8)
session.commit()

print ("added menu items!")
