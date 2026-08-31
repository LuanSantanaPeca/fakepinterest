from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
database_url = os.getenv("DATABASE_URL") or "sqlite:///comunidade.db"
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SECRET_KEY"] = "0fc9fc1a2655b6260117c619c41dbbb5"
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"

from fakepinterest import routes

pasta_fotos = os.path.join(os.path.dirname(__file__), app.config["UPLOAD_FOLDER"])
os.makedirs(pasta_fotos, exist_ok=True)

with app.app_context():
    database.create_all()
