
from rest_framework import serializers  # import de serializers
from assets.models import Monitormodels, Monitortypes, Monitors
from rest_framework import serializers
from assets.autoupdatesystems.serializers import AutoupdatesystemsSerializer
from assets.groups.serializers import GroupsSerializer
from assets.locations.serializers import LocationsSerializer
from assets.manufacturers.serializers import ManufacturersSerializer  # import de serializers
from assets.models import Locations, Manufacturers, Monitormodels, Monitors, Monitortypes, States
from assets.generics.serializers import EntitiesSerializer
from assets.states.serializers import StatesSerializer
from assets.users.serializers import UsersSerializer
class GetMonitortypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitortypes
        fields = ['id', 'name']

class GetMonitormodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitormodels
        fields = ['id', 'name']

class GetMonitorsCountSerializer(serializers.ModelSerializer):
    monitorsCount = serializers.SerializerMethodField()
    
    def get_monitorsCount(self,obj):
        return obj.count()
    
    class Meta:
        model = Monitors
        fields = ['monitorsCount']

class GetMonitorsCountByManufacturersSerializer(serializers.Serializer):
    manufacturers = serializers.CharField(source='manufacturers_id__name')
    count = serializers.IntegerField()
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

class GetMonitorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitors
        fields = ['id', 'name']

        
class CreateMonitorSerializer(serializers.ModelSerializer):

    class Meta:  # Clase meta para configurar el serializer
        model = Monitors  # Especificar el nombre del Model
        fields = '__all__'  # Para todos los atributos del model

class GetMonitorsByIdSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Monitors
        fields = ['id', 'name', 'states', 'locations', 'monitortypes', 'manufacturers', 'users_tech', 'groups_tech', 'groups', 'monitormodels', 'contact_num', 'serial', 'contact', 'otherserial', 'users', 'is_global', 'uuid', 'comment', 'size', 'autoupdatesystems', 'have_micro', 'have_speaker', 'have_subd', 'have_bnc', 'have_dvi', 'have_pivot', 'have_hdmi', 'have_displayport']

    def __init__(self, *args, **kwargs):
        item_id = kwargs.pop('item_id', None)
        super().__init__(*args, **kwargs)

        if item_id is not None:
            try:
                instance = Monitors.objects.get(id=item_id)
                self.instance = instance
            except Monitors.DoesNotExist:
                pass