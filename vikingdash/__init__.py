"""
VikingDash - By FRC6854
Under the CC0 License
"""

__name__ = "VikingDash"
__authors__ = ["Owen Shaule"]
__license__ = "CC0"

from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "Secret!")

print(f"""VikingDash Properties
Secret Key  : {SECRET_KEY}""")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

import vikingdash.models

with app.app_context():
    db.create_all()

import vikingdash.methods

@app.context_processor
def context_processor():
    return dict(american_time=vikingdash.methods.american_time, alliance_list=vikingdash.methods.alliance_list)

import vikingdash.routes