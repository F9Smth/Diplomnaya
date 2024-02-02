# queries.py
import src.bot
from src.db import db
from src.bot.models import Statistic
def get_stats():
    return db.session.query(Statistic).all()
