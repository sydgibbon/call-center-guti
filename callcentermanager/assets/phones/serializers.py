
from rest_framework import serializers
from assets.autoupdatesystems.serializers import AutoupdatesystemsSerializer
from assets.groups.serializers import GroupsSerializer
from assets.locations.serializers import LocationsSerializer
from assets.manufacturers.serializers import ManufacturersSerializer  # import de serializers
from assets.models import Locations, Manufacturers, Phones, Phonetypes, Phonemodels, Phonepowersupplies, States
from assets.serializers import EntitiesSerializer
from assets.states.serializers import StatesSerializer
from assets.users.serializers import UsersSerializer

class GetPhonesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = ['id', 'name']

class GetPhonetypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonetypes
        fields = ['id', 'name']

class GetPhonemodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonemodels
        fields = ['id', 'name']

class GetPhonepowersuppliesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonepowersupplies
        fields = ['id', 'name']

class PhonetypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonetypes
        fields = '__all__'

class PhonemodelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonemodels
        fields = '__all__'

class PhonepowersuppliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonepowersupplies
        fields = '__all__'

class PhonesSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    locations = LocationsSerializer(required=False)
    phonetypes = PhonetypesSerializer(required=False)
    phonemodels = PhonemodelsSerializer(required=False)
    phonepowersupplies = PhonepowersuppliesSerializer(required=False)
    manufacturers = ManufacturersSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    groups_tech = GroupsSerializer(required=False)
    users = UsersSerializer(required=False)
    groups = GroupsSerializer(required=False)
    autoupdatesystems = AutoupdatesystemsSerializer(required=False)
    states = StatesSerializer(required=False)

    class Meta:
        model = Phones
        fields = '__all__'

class GetPhonesSerializer(serializers.ModelSerializer):
    states = serializers.SerializerMethodField()
    manufacturers = serializers.SerializerMethodField()
    locations = serializers.SerializerMethodField()
    phonetypes = serializers.SerializerMethodField()
    phonemodels = serializers.SerializerMethodField()
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

    def get_phonetypes(self, obj):
        phonetypes = Phonetypes.objects.filter(id=obj.phonetypes_id)
        if (phonetypes.count() > 0):
            return Phonetypes.objects.filter(id=obj.phonetypes_id)[0].name
        return None
    
    def get_phonemodels(self, obj):
        phonemodels = Phonemodels.objects.filter(id=obj.phonemodels_id)
        if (phonemodels.count() > 0):
            return Phonemodels.objects.filter(id=obj.phonemodels_id)[0].name
        return None
    class Meta:
        model = Phones
        fields = ['id', 'name', 'states', 'manufacturers', 'locations', 'phonetypes', 'phonemodels', 
                  'date_mod', 'contact']
        
