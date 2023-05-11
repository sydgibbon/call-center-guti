from assets import serializers
from assets.autoupdatesystems.serializers import AutoupdatesystemsSerializer
from assets.groups.serializers import GroupsSerializer
from assets.locations.serializers import LocationsSerializer
from assets.manufacturers.serializers import ManufacturersSerializer
from assets.models import Unmanageds
from assets.networks.serializers import NetworksSerializer
from assets.states.serializers import StatesSerializer
from assets.users.serializers import UsersSerializer


class UnmanagedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unmanageds
        fields = '__all__'
      
class UnmanagedsSerializer(serializers.ModelSerializer):
    entities = serializers.EntitiesSerializer(required=False)
    locations = LocationsSerializer(required=False)
    networks = NetworksSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    users = UsersSerializer(required=False)
    groups = GroupsSerializer(required=False)
    autoupdatesystems = AutoupdatesystemsSerializer(required=False)
    states = StatesSerializer(required=False)

    class Meta:
        model = Unmanageds
        fields = '__all__'