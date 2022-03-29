from flask import request
from database import db, app

from models.vehicle_model import Vehicle
from schemas.vehicle_schema import vehicle_schema, vehicles_schema

@app.route('/vehicle', methods=["POST"])
def create_vehicle():
    Vehicle.__table__.create(db.session.bind, checkfirst=True)

    name = request.json['name']
    vehicle_class = request.json['vehicle_class']
    race = request.json['primary_race']
    status = request.json['status']

    newVehicle = Vehicle(name=name, vehcile_class=vehicle_class, primary_race=race, status=status)

    db.session.add(newVehicle)
    db.session.commit()

    vehicle = Vehicle.query.get(newVehicle.id)

    return vehicle_schema.jsonify(vehicle)

@app.route('/vehicles', methods=["GET"])
def get_all_vehicles():
    vehicles = Vehicle.query.all()
    return vehicles_schema.jsonify(vehicles)

@app.route('/vehicle/<id>', methods=["GET"])
def get_vehicle_by_id(id):
    vehicle = Vehicle.query.get(id)
    return vehicle_schema.jsonify(vehicle)

@app.route('/vehicle/<id>', methods=["PUT"])
def update_vehicle_by_id(id):
    name = request.json["name"]
    vehicle_class = request.json["vehicle_class"]
    primary_race = request.json["primary_race"]
    status = request.json["status"]

    vehicle = Vehicle.query.get(id)
    vehicle.name = name
    vehicle.vehicle_class = vehicle_class
    vehicle.primary_race = primary_race
    vehicle.status = status

    db.session.commit()

    updated_vehicle = Vehicle.query.get(id)
    return vehicle_schema.jsonify(updated_vehicle)

@app.route('/vehicle/<id>', methods=["DELETE"])
def delete_vehicle_by_id(id):
    vehicle = Vehicle.query.get(id)
    db.session.delete(vehicle)
    db.session.commit()

    return vehicle_schema.jsonify(vehicle)