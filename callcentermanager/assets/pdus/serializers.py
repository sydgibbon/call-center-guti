
from rest_framework import serializers
from assets.groups.serializers import GroupsSerializer
from assets.locations.serializers import LocationsSerializer
from assets.manufacturers.serializers import ManufacturersSerializer  # import de serializers
from assets.models import Pdus, PdusPlugs, PdusRacks, Pdutypes, Pdumodels
from assets.generics.serializers import EntitiesSerializer
from assets.states.serializers import StatesSerializer
from assets.users.serializers import UsersSerializer
from rest_framework import serializers  # import de serializers
from assets.models import Pdutypes, Pdumodels, Pdus

class GetPdutypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdutypes
        fields = ['id', 'name']

class GetPdumodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdumodels
        fields = ['id', 'name']

class GetPdusCountSerializer(serializers.ModelSerializer):
    pdusCount = serializers.SerializerMethodField()
    
    def get_pdusCount(self,obj):
        return obj.count()
    
    class Meta:
        model = Pdus
        fields = ['pdusCount']

class GetPdutypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdutypes
        fields = ['id', 'name']

class GetPdumodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdumodels
        fields = ['id', 'name']

class PdusPlugsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PdusPlugs
        fields = '__all__'

class PdusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdus
        fields = '__all__'

class PdutypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdutypes
        fields = '__all__'

class PdumodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdumodels
        fields = '__all__'
    
class PdusRacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = PdusRacks
        fields = '__all__'

class GetPdusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdus
        fields = ['id', 'name']

class PdusSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    locations = LocationsSerializer(required=False)
    pdumodels = PdumodelsSerializer(required=False)
    pdutypes = PdutypesSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    states = StatesSerializer(required=False)

    class Meta:
        model = Pdus
        fields = '__all__'

class GetPdusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdus
        fields = ['id', 'name']

class CreatePduSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdus
        fields = '__all__'

class GetPdusByIdSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Pdus
        fields = ['id', 'name', 'states', 'locations', 'pdutypes', 'users_tech', 'manufacturers', 'groups_tech', 'pdumodels', 'serial', 'otherserial', 'comment']

    def __init__(self, *args, **kwargs):
        item_id = kwargs.pop('item_id', None)
        super().__init__(*args, **kwargs)

        if item_id is not None:
            try:
                instance = Pdus.objects.get(id=item_id)
                self.instance = instance
            except Pdus.DoesNotExist:
                pass