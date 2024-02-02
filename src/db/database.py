# database.py
from .models import Statistic
from .queries import get_stats
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_tables():
    db.create_all()

def init_db(app):
    db.init_app(app)
    
