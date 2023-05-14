
from rest_framework import serializers
from assets.groups.serializers import GroupsSerializer
from assets.locations.serializers import LocationsSerializer
from assets.manufacturers.serializers import ManufacturersSerializer  # import de serializers
from assets.models import ItemsRacks, Racks, Racktypes, Rackmodels, Dcrooms
from assets.generals.serializers import EntitiesSerializer
from assets.states.serializers import StatesSerializer
from assets.users.serializers import UsersSerializer

class GetRacktypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Racktypes
        fields = ['id', 'name']

class GetRackmodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rackmodels
        fields = ['id', 'name']

class GetDcroomsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dcrooms
        fields = ['id', 'name']

class GetRacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Racks
        fields = ['id', 'name']

class ItemsRacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsRacks
        fields = '__all__'

class RackmodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rackmodels
        fields = '__all__'

class RacktypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Racktypes
        fields = '__all__'

class DcroomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dcrooms
        fields = '__all__'

class RacksSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    locations = LocationsSerializer(required=False)
    racktypes = RacktypesSerializer(required=False)
    rackmodels = RackmodelsSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    states = StatesSerializer(required=False)
    dcrooms = DcroomsSerializer(required=False)

    class Meta:
        model = Racks
        fields = '__all__'
