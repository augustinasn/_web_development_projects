from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "b9147debbf1525fbf88d3dcb7f14b511"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:mysecretpassword@localhost/postgres?port=5432"

db = SQLAlchemy(app)
ma = Marshmallow(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from homestorage import routes