from flask import request
from database import db, app

from models.character_model import Character
from schemas.character_schema import character_schema, characters_schema


@app.route('/character', methods=["POST"])
def createCharacter():
    Character.__table__.create(db.session.bind, checkfirst=True)
    first_name = request.json['first_name']
    middle_name = request.json['middle_name']
    last_name = request.json['last_name']
    rank = request.json['rank']
    description = request.json['description']
    status = request.json['status']
    actor = request.json['actor']
    affiliations = request.json['affiliations']

    new_character = Character(firstName=first_name, middleName=middle_name, lastName=last_name, rank=rank, description=description, status=status, actor=actor, affiliations=affiliations)

    db.session.add(new_character)
    db.session.commit()

    character =  Character.query.get(new_character.id)

    return character_schema.jsonify(character)


@app.route('/characters', methods=["GET"])
def get_characters():
    characters = Character.query.all()
    return characters_schema.jsonify(characters)

@app.route('/character/<id>', methods=["GET"])
def get_character_by_id(id):
    character = Character.query.get(id)

    return character_schema.jsonify(character)

@app.route('/character/<id>', methods=["PUT"])
def update_character_by_id(id):
    character = Character.query.get(id)
    first_name = request.json['first_name']
    middle_name = request.json['middle_name']
    last_name = request.json['last_name']
    rank = request.json['rank']
    description = request.json['description']
    status = request.json['status']
    actor = request.json['actor']
    affiliations = request.json['affiliations']

    character.first_name = first_name
    character.middle_name = middle_name
    character.last_name = last_name
    character.rank = rank
    character.description = description
    character.status = status
    character.actor = actor
    character.affiliations = affiliations

    db.session.commit()

    updated_character = Character.query.get(character.id)
    return character_schema.jsonify(updated_character)

@app.route('/character/<id>', methods=["DELETE"])
def remove_character_by_id(id):
    character = Character.query.get(id)
    db.session.delete(character)
    db.session.commit()

    return character_schema.jsonify(character)