from database import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.Text,unique=False, nullable=False)
    middle_name = db.Column(db.Text,unique=False, nullable=True)
    last_name = db.Column(db.Text, unique=False, nullable=True)
    rank = db.Column(db.Text, unique=False, nullable=True)
    description = db.Column(db.Text, unique=False, nullable=False)
    status = db.Column(db.Text, unique=False, nullable=False)
    actor = db.Column(db.Text, unique=False, nullable=False)
    affiliations = db.Column(db.Text, unique=False, nullable=False)

    def __init__(self, firstName, lastName,description, actor, affiliations,status = "Active", rank = None, middleName = None ):
        self.first_name = firstName
        self.middle_name = middleName
        self.last_name= lastName
        self.rank = rank
        self.description = description
        self.status = status
        self.actor = actor
        self.affiliations = affiliations