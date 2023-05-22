from rest_framework import serializers
from assets.autoupdatesystems.serializers import AutoupdatesystemsSerializer
from assets.groups.serializers import GroupsSerializer
from assets.locations.serializers import LocationsSerializer
from assets.manufacturers.serializers import ManufacturersSerializer  # import de serializers
from assets.models import Locations, Manufacturers, Peripherals, Peripheraltypes, Peripheralmodels, States
from assets.generics.serializers import EntitiesSerializer
from assets.states.serializers import StatesSerializer
from assets.users.serializers import UsersSerializer

class GetPeripheralsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peripherals
        fields = ['id', 'name']
        
class GetPeripheraltypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peripheraltypes
        fields = ['id', 'name']
        
class GetPeripheralmodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peripheralmodels
        fields = ['id', 'name']

class PeripheraltypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peripheraltypes
        fields = '__all__'


class PeripheralmodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peripheralmodels
        fields = '__all__'

class PeripheralsSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    locations = LocationsSerializer(required=False)
    peripheraltypes = PeripheraltypesSerializer(required=False)
    peripheralmodels = PeripheralmodelsSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users = UsersSerializer(required=False)
    groups = GroupsSerializer(required=False)
    states = StatesSerializer(required=False)
    autoupdatesystems = AutoupdatesystemsSerializer(required=False)

    class Meta:
        model = Peripherals
        fields = '__all__'

class GetPeripheralsSerializer(serializers.ModelSerializer):
    states = serializers.SerializerMethodField()
    manufacturers = serializers.SerializerMethodField()
    locations = serializers.SerializerMethodField()
    peripheraltypes = serializers.SerializerMethodField()
    peripheralmodels = serializers.SerializerMethodField()
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

    def get_peripheraltypes(self, obj):    
        peripheraltypes = Peripheraltypes.objects.filter(id=obj.peripheraltypes_id)
        if (peripheraltypes.count() > 0):
            return Peripheraltypes.objects.filter(id=obj.peripheraltypes_id)[0].name
        return None
    
    def get_peripheralmodels(self, obj):    
        peripheralmodels = Peripheralmodels.objects.filter(id=obj.peripheralmodels_id)
        if (peripheralmodels.count() > 0):
            return Peripheralmodels.objects.filter(id=obj.peripheralmodels_id)[0].name
        return None
    class Meta:
        model = Peripherals
        fields = ['id', 'name', 'states', 'manufacturers', 'locations', 'peripheraltypes', 'peripheralmodels', 
                  'date_mod', 'contact']
