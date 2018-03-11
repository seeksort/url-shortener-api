from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

urlapp = Flask(__name__)
urlapp.config.from_object(Config)
db = SQLAlchemy(urlapp)
migrate = Migrate(urlapp, db)

from app import routes, models
