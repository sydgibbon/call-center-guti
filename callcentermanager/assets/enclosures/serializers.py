
from rest_framework import serializers  # import de serializers
from assets.models import Enclosuremodels, Enclosures
from rest_framework import serializers
from assets.groups.serializers import GroupsSerializer
from assets.locations.serializers import LocationsSerializer
from assets.manufacturers.serializers import ManufacturersSerializer  # import de serializers
from assets.models import Enclosuremodels, Enclosures, ItemsEnclosures
from assets.generics.serializers import EntitiesSerializer
from assets.states.serializers import StatesSerializer
from assets.users.serializers import UsersSerializer

class GetEnclosuremodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enclosuremodels
        fields = ['id', 'name']

class GetEnclosuresCountSerializer(serializers.ModelSerializer):
    enclosuresCount = serializers.SerializerMethodField()
    
    def get_enclosuresCount(self,obj):
        return Enclosures.objects.count()
    
    class Meta:
        model = Enclosures
        fields = ['enclosuresCount']
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
