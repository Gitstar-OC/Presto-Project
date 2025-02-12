from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate 

app = Flask(__name__, static_folder='../frontend/dist')
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Notes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)