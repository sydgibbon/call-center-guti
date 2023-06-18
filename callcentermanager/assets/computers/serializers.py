
from rest_framework import serializers
from assets.autoupdatesystems.serializers import AutoupdatesystemsSerializer
from assets.locations.serializers import LocationsSerializer
from assets.manufacturers.serializers import ManufacturersSerializer  # import de serializers
from assets.models import Computers, Computermodels, ComputersItems, Computertypes, ItemsDeviceprocessors, ItemsOperatingsystems, Locations, Manufacturers, Operatingsystems, States
from assets.networks.serializers import NetworksSerializer
from assets.generics.serializers import EntitiesSerializer
from assets.states.serializers import StatesSerializer
from assets.users.serializers import UsersSerializer
from assets.groups.serializers import GroupsSerializer

class GetComputersSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computers
        fields = ['id', 'name']

class GetComputertypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computertypes
        fields = ['id', 'name']

class GetComputermodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computermodels
        fields = ['id', 'name']

class GetComputersCountSerializer(serializers.ModelSerializer):
    computersCount = serializers.SerializerMethodField()
    
    def get_computersCount(self,obj):
        return Computers.objects.count()
    
    class Meta:
        model = Computers
        fields = ['computersCount']

class GetComputersCountByManufacturersSerializer(serializers.Serializer):
    manufacturers = serializers.CharField(source='manufacturers_id__name')
    count = serializers.IntegerField()

class GetComputersCountByStatesSerializer(serializers.Serializer):

    states = serializers.CharField(source='states_id__name')
    count = serializers.IntegerField()

class GetComputersCountByComputertypesSerializer(serializers.Serializer):

    computertypes = serializers.CharField(source='computertypes_id__name')
    count = serializers.IntegerField()
class ComputertypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computertypes
        fields = '__all__'

class ComputermodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computermodels
        fields = '__all__'

class ComputersItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputersItems
        fields = '__all__'

class OperatingsystemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operatingsystems
        fields = '__all__'

class ComputersSerializer(serializers.ModelSerializer):
    computertypes = ComputertypesSerializer(required=False)
    computermodels = ComputermodelsSerializer(required=False)
    entities = EntitiesSerializer(required=False)
    networks = NetworksSerializer(required=False)
    locations = LocationsSerializer(required=False)
    autoupdatesystems = AutoupdatesystemsSerializer(required=False)
    users = UsersSerializer(required=False)
    groups = GroupsSerializer(required=False)
    states = StatesSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    # clase serializer con forma [NombreDeModel]Serializer(serializers.ModelSerializer)

    class Meta:  # Clase meta para configurar el serializer
        model = Computers  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model

class CreateComputerSerializer(serializers.ModelSerializer):

    class Meta:  # Clase meta para configurar el serializer
        model = Computers  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model

class GetComputersSerializer(serializers.ModelSerializer):
    states = serializers.SerializerMethodField()
    manufacturers = serializers.SerializerMethodField()
    computertypes = serializers.SerializerMethodField()
    computermodels = serializers.SerializerMethodField()
    operatingsystems = serializers.SerializerMethodField()
    locations = serializers.SerializerMethodField()
    date_mod = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    processors = serializers.SerializerMethodField()

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

    def get_computertypes(self, obj):
        computers = Computers.objects.filter(id=obj.computertypes_id)
        if (computers.count() > 0):
            return Computertypes.objects.filter(id=obj.computertypes_id)[0].name
        return None
    
    def get_computermodels(self, obj):
        computermodels = Computermodels.objects.filter(id=obj.computermodels_id)
        if (computermodels.count() > 0):
            return Computermodels.objects.filter(id=obj.computermodels_id)[0].name
        return None
    
    def get_operatingsystems(self, obj):
        items_operatingsystems = ItemsOperatingsystems.objects.filter(items_id=obj.id, itemtype='Computer')
        if (items_operatingsystems.count() > 0):
            return Operatingsystems.objects.filter(id=items_operatingsystems[0].operatingsystems_id)[0].name
        return None
            
    
    def get_locations(self, obj):
        locations = Locations.objects.filter(id=obj.locations_id)
        if (locations.count() > 0):
            return Locations.objects.filter(id=obj.locations_id)[0].name
        return None
    
    def get_processors(self, obj):
        items_deviceprocessors = ItemsDeviceprocessors.objects.filter(items_id=obj.id, itemtype='Computer')
        print(items_deviceprocessors)
        if (items_deviceprocessors.count() > 0):
            return items_deviceprocessors.count()
        return None
    
    class Meta:
        model = Computers
        fields = ['id', 'name', 'states', 'manufacturers', 'serial', 'computertypes', 'computermodels',
                  'operatingsystems', 'locations', 'date_mod', 'processors']

class GetComputersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computers
        fields = ['id', 'name']