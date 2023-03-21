"""
VikingDash - By FRC6854
Under the CC0 License
"""

__name__ = "VikingDash"
__authors__ = ["Owen Shaule"]
__license__ = "CC0"

from flask import Flask
from dotenv import load_dotenv
from flask_socketio import SocketIO
from pymongo import MongoClient
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "Secret!")
MONGODB_KEY = os.getenv("MONGODB_KEY", None)

print(f"""VikingDash Properties
Secret Key  : {SECRET_KEY}
MONGODB Key : {MONGODB_KEY}""")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
socketio = SocketIO(app)

if MONGODB_KEY: mongodb_client = MongoClient(MONGODB_KEY)
else: mongodb_client = MongoClient()

database = mongodb_client["VikingDash"]
coopertitions = database.coopertitions
users = database.users

import vikingdash.routes