
from rest_framework import serializers
from assets.autoupdatesystems.serializers import AutoupdatesystemsSerializer
from assets.groups.serializers import GroupsSerializer  # import de serializers
from assets.models import Locations, Manufacturers, Monitormodels, Monitors, Monitortypes, States
from assets.serializers import EntitiesSerializer, LocationsSerializer, ManufacturersSerializer, StatesSerializer, UsersSerializer
class GetMonitortypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitortypes
        fields = ['id', 'name']

class GetMonitormodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitormodels
        fields = ['id', 'name']

class MonitormodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitormodels
        fields = '__all__'


class MonitortypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitortypes
        fields = '__all__'

class MonitorsSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    locations = LocationsSerializer(required=False)
    monitortypes = MonitortypesSerializer(required=False)
    monitormodels = MonitormodelsSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users = UsersSerializer(required=False)
    groups = GroupsSerializer(required=False)
    states = StatesSerializer(required=False)
    autoupdatesystems = AutoupdatesystemsSerializer(required=False)

    class Meta:
        model = Monitors
        fields = '__all__'

class GetMonitorsSerializer(serializers.ModelSerializer):
    states = serializers.SerializerMethodField()
    manufacturers = serializers.SerializerMethodField()
    locations = serializers.SerializerMethodField()
    monitortypes = serializers.SerializerMethodField()
    monitormodels = serializers.SerializerMethodField()
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
                
    def get_locations(self, obj):
        locations = Locations.objects.filter(id=obj.locations_id)
        if (locations.count() > 0):
            return Locations.objects.filter(id=obj.locations_id)[0].name
        return None

    def get_monitortypes(self, obj):  
        monitortypes = Monitortypes.objects.filter(id=obj.monitortypes_id)
        if (monitortypes.count() > 0):
            return Monitortypes.objects.filter(id=obj.monitortypes_id)[0].name
        return None
    
    def get_monitormodels(self, obj):    
        monitormodels = Monitormodels.objects.filter(id=obj.monitormodels_id)
        if (monitormodels.count() > 0):
            return Monitormodels.objects.filter(id=obj.monitormodels_id)[0].name
        return None
    class Meta:
        model = Monitors
        fields = ['id', 'name', 'states', 'manufacturers', 'locations', 'monitortypes', 'monitormodels', 
                  'date_mod', 'contact']