
from rest_framework import serializers
from assets.groups.serializers import GroupsSerializer  # import de serializers
from assets.models import Enclosuremodels, Enclosures, ItemsEnclosures
from assets.serializers import EntitiesSerializer, LocationsSerializer, ManufacturersSerializer, StatesSerializer, UsersSerializer

class GetEnclosuremodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enclosuremodels
        fields = ['id', 'name']

class ItemsEnclosuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsEnclosures
        fields = '__all__'


class EnclosuremodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enclosuremodels
        fields = '__all__'

class EnclosuresSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    locations = LocationsSerializer(required=False)
    enclosuremodels = EnclosuremodelsSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    states = StatesSerializer(required=False)

    class Meta:
        model = Enclosures
        fields = '__all__'


class GetEnclosuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enclosures
        fields = ['id', 'name']
