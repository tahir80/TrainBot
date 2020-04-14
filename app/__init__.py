#app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_session import Session
db = SQLAlchemy()

bootstrap = Bootstrap()
login_manager = LoginManager()

# we need to tell Flask about the login view
login_manager.login_view = 'authentication.do_the_login'
# we can set the level of security, in this case, we chose strong.
# the flask will delete the session or cookies and forces the user to login again
# to protect the data
login_manager.session_protection = 'strong'

bcrypt = Bcrypt()


def create_app(config_type):

    app = Flask(__name__)

    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    #  to load the configuration file
    app.config.from_pyfile(configuration)

    #  to attach the Flask app with DB instance created on line # 7
    db.init_app(app)

    #you also need to initialize Bootstrap with flask ( or integgrate flask app with bootstrap)
    bootstrap.init_app(app)

    login_manager.init_app(app)
    bcrypt.init_app(app)

    # import Blueprint variable (authentication) from auth sub-package
    # from app.auth import authentication   # import blueprint (the name was main)
    # app.register_blueprint(authentication) # register blueprint

    from app.training import training
    app.register_blueprint(training)

    return app
