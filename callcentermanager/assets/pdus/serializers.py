
from rest_framework import serializers
from assets.groups.serializers import GroupsSerializer
from assets.locations.serializers import LocationsSerializer
from assets.manufacturers.serializers import ManufacturersSerializer  # import de serializers
from assets.models import Pdus, PdusPlugs, PdusRacks, Pdutypes, Pdumodels
from assets.generals.serializers import EntitiesSerializer
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
        return Pdus.objects.count()
    
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

