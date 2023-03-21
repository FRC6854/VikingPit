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

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

import vikingdash.routes