
from rest_framework import serializers  # import de serializers
from assets.models import Racktypes, Rackmodels, Dcrooms, Racks
from rest_framework import serializers
from assets.groups.serializers import GroupsSerializer
from assets.locations.serializers import LocationsSerializer
from assets.manufacturers.serializers import ManufacturersSerializer  # import de serializers
from assets.models import ItemsRacks, Racks, Racktypes, Rackmodels, Dcrooms
from assets.generics.serializers import EntitiesSerializer
from assets.states.serializers import StatesSerializer
from assets.users.serializers import UsersSerializer

class GetRacktypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Racktypes
        fields = ['id', 'name']

class GetRackmodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rackmodels
        fields = ['id', 'name']

class GetDcroomsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dcrooms
        fields = ['id', 'name']

class GetRacksCountSerializer(serializers.ModelSerializer):
    racksCount = serializers.SerializerMethodField()
    
    def get_racksCount(self,obj):
        return obj.count()
    
    class Meta:
        model = Racks
        fields = ['racksCount']
class GetRacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Racks
        fields = ['id', 'name']

class ItemsRacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsRacks
        fields = '__all__'

class RackmodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rackmodels
        fields = '__all__'

class RacktypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Racktypes
        fields = '__all__'

class DcroomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dcrooms
        fields = '__all__'

class RacksSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    locations = LocationsSerializer(required=False)
    racktypes = RacktypesSerializer(required=False)
    rackmodels = RackmodelsSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    states = StatesSerializer(required=False)
    dcrooms = DcroomsSerializer(required=False)

    class Meta:
        model = Racks
        fields = '__all__'

class GetRacksListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Racks
        fields = ['id', 'name']
        
class CreateRackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Racks
        fields = '__all__'

class GetRacksByIdSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Racks
        fields = ['id', 'name', 'states', 'dcrooms', 'locations', 'racktypes', 'users_tech', 'manufacturers', 'groups_tech', 'rackmodels', 'serial', 'otherserial', 'comment', 'position', 'room_orientation', 'number_units', 'width', 'height', 'depth', 'max_power', 'mesured_power', 'max_weight', 'bgcolor']

    def __init__(self, *args, **kwargs):
        item_id = kwargs.pop('item_id', None)
        super().__init__(*args, **kwargs)

        if item_id is not None:
            try:
                instance = Racks.objects.get(id=item_id)
                self.instance = instance
            except Racks.DoesNotExist:
                pass