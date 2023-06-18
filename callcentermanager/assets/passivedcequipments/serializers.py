
from rest_framework import serializers
from assets.groups.serializers import GroupsSerializer
from assets.locations.serializers import LocationsSerializer
from assets.manufacturers.serializers import ManufacturersSerializer  # import de serializers
from assets.models import Passivedcequipments, Passivedcequipmenttypes, Passivedcequipmentmodels, Pdus
from assets.generics.serializers import EntitiesSerializer
from assets.states.serializers import StatesSerializer
from assets.users.serializers import UsersSerializer

class GetPassivedcequipmentsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passivedcequipments
        fields = ['id', 'name']

class GetPassivedcequipmenttypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passivedcequipmenttypes
        fields = ['id', 'name']

class GetPassivedcequipmentmodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passivedcequipmentmodels
        fields = ['id', 'name']

class PassivedcequipmentmodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passivedcequipmentmodels
        fields = '__all__'

class PassivedcequipmenttypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passivedcequipmenttypes
        fields = '__all__'

class GetPassivedcequipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdus
        fields = ['id', 'name']

class PassivedcequipmentsSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    locations = LocationsSerializer(required=False)
    passivedcequipmentmodels = PassivedcequipmentmodelsSerializer(required=False)
    passivedcequipmenttypes = PassivedcequipmenttypesSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    states = StatesSerializer(required=False)

    class Meta:
        model = Passivedcequipments
        fields = '__all__'

class GetPassivedcequipmentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passivedcequipments
        fields = ['id', 'name']

class CreatePassivedcequipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passivedcequipments
        fields = '__all__'
