from dataclasses import dataclass
from vikingdash import db
import sqlalchemy as sa

class Coopertition(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    red = sa.Column(sa.String, nullable=False)
    blue = sa.Column(sa.String, nullable=False)
    name = sa.Column(sa.String, nullable=False)
    time = sa.Column(sa.String, nullable=False)
    completed = sa.Column(sa.Boolean, nullable=False)
    redname = sa.Column(sa.String, nullable=False)
    bluename = sa.Column(sa.String, nullable=False)
    redpoints = sa.Column(sa.Integer, nullable=True)
    bluepoints = sa.Column(sa.Integer, nullable=True)

class Status:
    def __init__(self, status):
        self.status = status

    def set_status(self, status):
        self.status = status

    def __repr__(self):
        return f"Status({self.status})"
    
    def __str__(self):
        return self.status
    
class Reloader:
    def __init__(self) -> None:
        self.reload = False

    def __repr__(self) -> str:
        return f"Reloader({self.reload})"