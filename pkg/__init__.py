# from config import BASE_DIR, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD
# Import flask and template operators
from flask import Flask, render_template, request, send_from_directory
from flask import session as login_session
from flask.ext.login import LoginManager
# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Import Bootstrap
from flask_bootstrap import Bootstrap

import json
import os

app = Flask(__name__)
db = SQLAlchemy(app)
# Import a module/component using its blueprint handler variable (mod_auth)
from pkg.auth.views import mod_auth as auth_module
from pkg.restaurant.views import restaurant_b
from pkg.api.views import api_b
from pkg.menu_item.views import menu_b
from pkg.fron_end.views import index_b


def set_db_session(session):
    print("In set db_session")
    app.db_session = session


def set_login_session_user_id(userid):
    app.secret_key = 'super_secret_key'
    login_session['user_id'] = userid
    print ("In set_login_session_user_id: {}".format(login_session))


def create_app(app, db, debug=False):
    # Define the WSGI application object
    app.debug = debug

    # Configurations
    if debug:
        app.config.from_object('config.DebugConfiguration')
    else:
        app.config.from_object('config.BaseConfiguration')

    # Define the database object which is imported 
    # by modules and controllers
    Bootstrap(app)
    # Register blueprint(s)
    app.register_blueprint(auth_module)
    app.register_blueprint(restaurant_b, url_prefix='/restaurants')
    app.register_blueprint(menu_b)
    app.register_blueprint(api_b, url_prefix='/restaurants/developers')
    app.register_blueprint(index_b)
    app.db_session = db.session

    APPLICATION_NAME = "Restaurant Menu Application"

    # if not app.debug:
    #     import logging
    #     from logging.handlers import SMTPHandler
    #     credentials = None
    #     if MAIL_USERNAME or MAIL_PASSWORD:
    #         credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    #     mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@' + MAIL_SERVER, ADMINS, 'restaurant failure', credentials)
    #     mail_handler.setLevel(logging.ERROR)
    #     app.logger.addHandler(mail_handler)
    #
    # if not app.debug:
    #     import logging
    #     from logging.handlers import RotatingFileHandler
    #     file_handler = RotatingFileHandler('tmp/restaurant.log', 'a', 1 * 1024 * 1024, 10)
    #     file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    #     app.logger.setLevel(logging.INFO)
    #     file_handler.setLevel(logging.INFO)
    #     app.logger.addHandler(file_handler)
    #     app.logger.info('restaurant startup')
    return db


def not_found(error):
    return render_template('404.html'), 404
# Sample HTTP error handling
# @app.errorhandler(404)
