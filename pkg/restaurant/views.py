
from flask import Flask, render_template, request, redirect,jsonify, url_for, flash, Blueprint
from flask import session as login_session
from flask.ext.sqlalchemy import SQLAlchemy
from flask import make_response
from sqlalchemy import desc

# from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION

from pkg import app
from pkg import db
from pkg.auth.models import User
from pkg.restaurant.models import Restaurant, RestaurantAddress
from pkg.menu_item.models import MenuItem
from pkg.auth.views import login_required

from markupsafe import escape

from .forms import RestaurantForm


restaurant_b = Blueprint('restaurant_b', __name__)


@restaurant_b.route('/')
def show_restaurants():
    """Created route and function to display the
       restaurant list """
    restaurants = app.db_session.query(Restaurant).order_by(desc(Restaurant.name))
    if restaurants:
        if 'user_id' in login_session:
            print ('user_id in login_session')
            return render_template('restaurant/restaurants.html', restaurants=restaurants, hello="database found")
        else:
            print ('user_id not in login_session')
            return render_template('restaurant/restaurants.html', restaurants=restaurants)
    else:
        return render_template('restaurant/restaurants.html', restaurants=restaurants, hello="no database")


@restaurant_b.route('/<int:restaurant_id>/menu/')
@restaurant_b.route('/<int:restaurant_id>/')
def restaurant_detail(restaurant_id):
    """Created route and function to display the
        restaurant main page and menu individually"""
    try:
        restaurant = app.db_session.query(Restaurant).filter_by(id=restaurant_id).one()
        address = app.db_session.query(RestaurantAddress).filter_by(id=restaurant_id).one()
        items = app.db_session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
        return render_template("restaurant/restaurantownpage.html", restaurant=restaurant, items=items, address=address)

    except:
        return render_template("restaurant/restaurants.html", error="Restaurant Not Found")


@restaurant_b.route('/new', methods=['GET', 'POST'])
@login_required
def create_restaurant():
    form = RestaurantForm()

    if form.validate_on_submit():
        add_values = Restaurant(name=form.name.data,
                                phone=form.phone.data,
                                food_type=form.course.data,
                                email=form.email.data,
                                website=form.website.data,
                                description=form.description.data,
                                user_id=login_session['user_id'])
        app.db_session.add(add_values)
        app.db_session.commit()
        app.db_session.refresh(add_values)
        add_address = RestaurantAddress(street=form.street.data,
                                        city=form.city.data,
                                        state=form.state.data,
                                        zip_code=form.zip_code.data,
                                        restaurant_id=add_values.id)
        app.db_session.add(add_address)
        app.db_session.commit()
        flash("New restaurant Created")
        return redirect(url_for('.show_restaurants'))

    else:
        return render_template("restaurant/newRestaurant.html", form=form)


@restaurant_b.route('/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
@login_required
def delete_restaurant(restaurant_id):
    """Created route and function to delete restaurants individually"""
    if Restaurant.user_creator(login_session['user_id'], restaurant_id):
        restaurant = app.db_session.query(Restaurant).filter_by(id=restaurant_id).one()
        address = app.db_session.query(RestaurantAddress).filter_by(restaurant_id=restaurant.id).one()
        if request.method == 'POST':
            app.db_session.delete(address)
            app.db_session.delete(restaurant)
            app.db_session.commit()
            flash("Your Restaurant have been deleted")
            return redirect(url_for('.show_restaurants'))

        return render_template("restaurant/deleteRestaurant.html", restaurant=restaurant)
    else:
        flash("You cannot made any changes, make your own restaurant and try again")
        return redirect(url_for('.show_restaurants'))


@restaurant_b.route('/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
@login_required
def edit_restaurant(restaurant_id):
    """Created route and function to edit restaurants"""
    if Restaurant.user_creator(login_session['user_id'], restaurant_id):
        restaurant = app.db_session.query(Restaurant).filter_by(id=restaurant_id).one()
        address = app.db_session.query(RestaurantAddress).filter_by(restaurant_id=restaurant.id).one()
        form = RestaurantForm()
        if form.validate_on_submit():
            restaurant.name = form.name.data
            restaurant.phone = form.phone.data
            restaurant.email = form.email.data
            restaurant.course = form.course.data
            restaurant.description = form.description.data
            restaurant.website = form.website.data
            app.db_session.add(restaurant)

            app.db_session.commit()
            app.db_session.refresh(restaurant)
            address.street = form.street.data
            address.city = form.city.data
            address.state = form.state.data
            address.zip_code = form.zip_code.data
            app.db_session.add(address)
            app.db_session.commit()
            flash("Your restaurant have been edited successfully")
            return redirect(url_for('.show_restaurants'))
        else:
            form.description.data = restaurant.description
            return render_template("restaurant/editrestaurant.html", form=form, restaurant=restaurant, address=address)
    else:
        flash("You cannot made any changes, make your own restaurant and try again")
        return redirect(url_for('.show_restaurants'))
