from rest_framework import serializers
from assets.autoupdatesystems.serializers import AutoupdatesystemsSerializer
from assets.groups.serializers import GroupsSerializer
from assets.locations.serializers import LocationsSerializer
from assets.manufacturers.serializers import ManufacturersSerializer  # import de serializers
from assets.models import Locations, Manufacturers, Printers, Printermodels, PrintersCartridgeinfos, Printertypes, States
from assets.networks.serializers import NetworksSerializer
from assets.generics.serializers import EntitiesSerializer
from assets.snmpcredentials.serializers import SnmpcredentialsSerializer
from assets.states.serializers import StatesSerializer
from assets.users.serializers import UsersSerializer

class GetPrintersSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printers
        fields = ['id', 'name']

class GetPrintermodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printermodels
        fields = ['id', 'name']
class GetPrintertypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printertypes
        fields = ['id', 'name']

class GetPrintersCountSerializer(serializers.ModelSerializer):
    printersCount = serializers.SerializerMethodField()
    
    def get_printersCount(self,obj):
        return Printers.objects.count()
    
    class Meta:
        model = Printers
        fields = ['printersCount']
class PrintermodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printermodels
        fields = '__all__'


class PrintertypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printertypes
        fields = '__all__'


class PrintersCartridgeinfosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintersCartridgeinfos
        fields = '__all__'

class PrintersSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    locations = LocationsSerializer(required=False)
    networks = NetworksSerializer(required=False)
    printermodels = PrintermodelsSerializer(required=False)
    printertypes = PrintertypesSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users = UsersSerializer(required=False)
    groups = GroupsSerializer(required=False)
    states = StatesSerializer(required=False)
    snmpcredentials = SnmpcredentialsSerializer(required=False)
    autoupdatesystems = AutoupdatesystemsSerializer(required=False)

    class Meta:
        model = Printers
        fields = '__all__'

class GetPrintersSerializer(serializers.ModelSerializer):
    states = serializers.SerializerMethodField()
    manufacturers = serializers.SerializerMethodField()
    locations = serializers.SerializerMethodField()
    printertypes = serializers.SerializerMethodField()
    printermodels = serializers.SerializerMethodField()
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

    def get_printertypes(self, obj):
        printertypes = Printertypes.objects.filter(id=obj.printertypes_id)
        if (printertypes.count() > 0):
            return Printertypes.objects.filter(id=obj.printertypes_id)[0].name
        return None
    
    def get_printermodels(self, obj):
        printermodels = Printermodels.objects.filter(id=obj.printermodels_id)
        if (printermodels.count() > 0):
            return Printermodels.objects.filter(id=obj.printermodels_id)[0].name
        return None
    class Meta:
        model = Printers
        fields = ['id', 'name', 'states', 'manufacturers', 'locations', 'printertypes', 'printermodels', 
                  'date_mod']

class GetPrintersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printers
        fields = ['id', 'name']
        
class CreatePrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printers
        fields = '__all__'
