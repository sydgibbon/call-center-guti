
from rest_framework import serializers
from assets.autoupdatesystems.serializers import AutoupdatesystemsSerializer
from assets.groups.serializers import GroupsSerializer
from assets.locations.serializers import LocationsSerializer
from assets.manufacturers.serializers import ManufacturersSerializer  # import de serializers
from assets.models import Devicefirmwares, ItemsDevicefirmwares, Locations, Manufacturers, Networkequipments, Networkequipmenttypes, Networkequipmentmodels, States
from assets.generics.serializers import EntitiesSerializer, NetworksSerializer
from assets.snmpcredentials.serializers import SnmpcredentialsSerializer
from assets.states.serializers import StatesSerializer
from assets.users.serializers import UsersSerializer

class GetNetworkequipmentsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networkequipments
        fields = ['id', 'name']

class GetNetworkequipmenttypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networkequipmenttypes
        fields = ['id', 'name']

class GetNetworkequipmentmodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networkequipmentmodels
        fields = ['id', 'name']

class NetworkequipmentmodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networkequipmentmodels
        fields = '__all__'

class NetworkequipmenttypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networkequipmenttypes
        fields = '__all__'

class NetworkequipmentsSerializer(serializers.ModelSerializer):
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    locations = LocationsSerializer(required=False)
    networks = NetworksSerializer(required=False)
    networkequipmenttypes = NetworkequipmenttypesSerializer(required=False)
    networkequipmentmodels = NetworkequipmentmodelsSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users = UsersSerializer(required=False)
    groups = GroupsSerializer(required=False)
    states = StatesSerializer(required=False)
    autoupdatesystems = AutoupdatesystemsSerializer(required=False)
    snmpcredentials = SnmpcredentialsSerializer(required=False)
    entities = EntitiesSerializer(required=False)

    class Meta:
        model = Networkequipments
        fields = '__all__'

class GetNetworkequipmentsSerializer(serializers.ModelSerializer):
    states = serializers.SerializerMethodField()
    manufacturers = serializers.SerializerMethodField()
    networkequipmenttypes = serializers.SerializerMethodField()
    networkequipmentmodels = serializers.SerializerMethodField()
    devicefirmwares = serializers.SerializerMethodField()
    locations = serializers.SerializerMethodField()
    date_mod = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    def get_states(self, obj):
        states = States.objects.filter(id=obj.manufacturers_id)
        if (states.count() > 0):
            return States.objects.filter(id=obj.states_id)[0].name
        return None

    def get_manufacturers(self, obj):
        manufacturers = Manufacturers.objects.filter(id=obj.manufacturers_id)
        if (manufacturers.count() > 0):
            return Manufacturers.objects.filter(id=obj.manufacturers_id)[0].name
        return None
    
    def get_networkequipmenttypes(self, obj):
        networkequipmenttypes = Networkequipmenttypes.objects.filter(id=obj.manufacturers_id)
        if (networkequipmenttypes.count() > 0):
            return Networkequipmenttypes.objects.filter(id=obj.networkequipmenttypes_id)[0].name
        return None
    
    def get_networkequipmentmodels(self, obj):    
        networkequipmentmodels = Networkequipmentmodels.objects.filter(id=obj.manufacturers_id)
        if (networkequipmentmodels.count() > 0):
            return Networkequipmentmodels.objects.filter(id=obj.networkequipmentmodels_id)[0].name
        return None
    
    def get_devicefirmwares(self, obj):
        items_devicefirmwares = ItemsDevicefirmwares.objects.filter(items_id=obj.id, itemtype='NetworkEquipment')
        if (items_devicefirmwares.count() > 0):
            return Devicefirmwares.objects.filter(id=items_devicefirmwares[0].devicefirmwares_id)[0].version
        return None
    
    def get_locations(self, obj):
        locations = Locations.objects.filter(id=obj.locations_id)
        if (locations.count() > 0):
            return Locations.objects.filter(id=obj.locations_id)[0].name
        return None
    
    class Meta:
        model = Networkequipments
        fields = ['id', 'name', 'states', 'manufacturers', 'locations', 'networkequipmenttypes', 'networkequipmentmodels',
                  'devicefirmwares', 'date_mod']

class GetNetworkequipmentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networkequipments
        fields = ['id', 'name']