# from config import BASE_DIR, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD
# Import flask and template operators
from flask import Flask
from flask import session as login_session
# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Import Bootstrap
from flask_bootstrap import Bootstrap

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

    return db
