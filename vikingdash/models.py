from dataclasses import dataclass

@dataclass
class Coopertition:
    red : list
    blue : list
    name : str
    time : str # PyMongo has no time object, ugh
    completed = False
    redname : str
    bluename : str

    def export(self):
        return {
            "red": self.red,
            "blue": self.blue,
            "name": self.name,
            "time": self.time,
            "completed": self.completed,
            "redname": self.redname,
            "bluename": self.bluename
        }

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