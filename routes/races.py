from flask import request
from database import db, app

from models.race_model import Race
from schemas.race_schema import race_schema, races_schema

@app.route('/race', methods=["POST"])
def createRace():
    Race.__table__.create(db.session.bind, checkfirst=True)
    tables = db.engine.table_names()
    print(tables)

    name = request.json['name']
    home_world = request.json['home_world']

    newRace = Race(name=name, homeWorld=home_world)
    print(newRace)
    dbsessionadd = db.session.add(newRace)
    print(dbsessionadd)
    db.session.commit()
    race = Race.query.get(newRace.id)

    return race_schema.jsonify(race)

@app.route('/races', methods=["GET"])
def getRaces():
    all_races = Race.query.all()
    return races_schema.jsonify(all_races)

@app.route('/race/<id>', methods=["GET"])
def get_race_by_id(id):
    race = Race.query.get(id)

    return race_schema.jsonify(race)

@app.route('/race/<id>', methods=["PUT"])
def update_race_by_id(id):
    name = request.json["name"]
    home_world = request.json["home_world"]

    race = Race.query.get(id)
    race.name = name
    race.home_world = home_world

    db.session.commit()

    updated_race = Race.query.get(id)

    return race_schema.jsonify(updated_race)

@app.route('/race/<id>', methods=["DELETE"])
def delete_race_by_id(id):
    race = Race.query.get(id)
    db.session.delete(race)
    db.session.commit()

    return race_schema.jsonify(race)