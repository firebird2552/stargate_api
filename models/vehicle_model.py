from database import db

class Vehicle(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.Text, unique=True, nullable=False)
    vehicle_class = db.Column(db.Text, unique=False, nullable=False)
    primary_race = db.Column(db.Text, unique=False, nullable=False)
    status = db.Column(db.Text, unique=False, nullable=False)

    def __init__(self, name, vehcile_class, primary_race, status):
        self.name = name
        self.vehicle_class = vehcile_class
        self.primary_race = primary_race
        self.status = status