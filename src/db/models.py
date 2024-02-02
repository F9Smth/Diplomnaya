# models.py
from database import db
import .queries
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

class Statistic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String)
    execution_time = db.Column(db.Integer)
    # other model fields here

Base = declarative_base() 

class User(Base):

  __tablename__ = 'users'
  
  id = Column(Integer, primary_key=True)
  name = Column(String)
  age = Column(Integer)

class Post(Base):

  __tablename__ = 'posts'
  
  id = Column(Integer, primary_key=True)
  title = Column(String)
  content = Column(Text)
  user_id = Column(Integer, ForeignKey('users.id'))

