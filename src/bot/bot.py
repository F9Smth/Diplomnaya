from aiogram import Bot, Dispatcher, executor, types
from database import Database
from .commands import Commands
from .conversations import Conversations

#Create a database and enter some data
db = Database("statistics.db")
db.create_statistics_table()
db.insert_statistics("SELECT * FROM users", 10, 100, 1000, 10, 10)
db.insert_statistics("SELECT * FROM orders", 20, 200, 2000, 20, 20)

#Get statistical data
stats = db.get_statistics()
for row in stats:
    print(row)

class Bot:
    """Bot class for managing bot lifecycle and handlers."""
    
    def __init__(self):
        """Initialize bot components."""
        self.commands = Commands()
        self.conversations = Conversations()
    
    def run(self):
        """Run bot event loop."""
        ...