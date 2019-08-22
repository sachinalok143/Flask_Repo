
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config
app=Flask(__name__)

from flaskblog.errors.handlers import errors

db=SQLAlchemy(app)

bcrypt=Bcrypt(app)
app.config.from_object(Config)

app.register_blueprint(errors)

login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'


mail=Mail(app)

from flaskblog import routes
