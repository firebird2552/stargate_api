from database import mallow

class VehicleSchema(mallow.Schema):
    class Meta:
        fields = ('id', 'name', 'vehicle_class', 'primary_race', 'status')

vehicle_schema = VehicleSchema()
vehicles_schema = VehicleSchema(many=True)