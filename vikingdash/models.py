from dataclasses import dataclass

@dataclass
class Coopertition:
    red_alliance : list
    blue_alliance : list
    red_points : any # Can be None or a Int
    blue_points: any # Can be None or a Int
    name : str
    time : str # PyMongo has no time object, ugh