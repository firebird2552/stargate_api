from database import mallow

class CharacterSchema(mallow.Schema):
    class Meta:
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'rank', 'description', 'status', 'actor', "affiliations")

character_schema = CharacterSchema()
characters_schema = CharacterSchema(many=True)