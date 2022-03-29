from database import mallow

class RaceSchema(mallow.Schema):
    class Meta:
        fields = ('id', 'name', 'home_world')

race_schema = RaceSchema()
races_schema = RaceSchema(many=True)