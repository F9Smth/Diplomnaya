from aiogram import Bot, Dispatcher, executor, types
from database import Database

#Создать бд и ввести некоторые данные в неё
db = Database("statistics.db")
db.create_statistics_table()
db.insert_statistics("SELECT * FROM users", 10, 100, 1000, 10, 10)
db.insert_statistics("SELECT * FROM orders", 20, 200, 2000, 20, 20)

#Получить статистические данные
statistics = db.get_statistics()
for row in statistics:
    print(row)
    

# bot.py

from .commands import Commands
from .conversations import Conversations

class Bot:
  def __init__(self):
    self.commands = Commands()
    self.conversations = Conversations()
  
  def run(self):
    # code to run bot
