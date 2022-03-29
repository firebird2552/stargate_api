from database import db

class Race(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.Text, unique = True, nullable=False)
    home_world = db.Column(db.Text, unique=False, nullable=False)

    def __init__(self, name, homeWorld):
        self.name = name
        self.home_world = homeWorld