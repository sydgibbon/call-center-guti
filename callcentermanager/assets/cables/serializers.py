
from rest_framework import serializers  # import de serializers
from assets.models import Cables, Cabletypes, Cablestrands, Sockets, Socketmodels, States, Users
from assets.generics.serializers import EntitiesSerializer
from assets.states.serializers import StatesSerializer
from assets.users.serializers import UsersSerializer

class GetCabletypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabletypes
        fields = ['id', 'name']
        
class GetCablestrandsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cablestrands
        fields = ['id', 'name']
                      
class GetSocketsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sockets
        fields = ['id', 'name']

class GetSocketmodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socketmodels
        fields = ['id', 'name']

class GetCablesSerializer(serializers.ModelSerializer):
    cabletypes = serializers.SerializerMethodField()
    states = serializers.SerializerMethodField()
    users_tech = serializers.SerializerMethodField()

    def get_cabletypes(self, obj):
        if (Cabletypes.objects.filter(id=obj.cabletypes_id).count() > 0):
            return Cabletypes.objects.filter(id=obj.cabletypes_id)[0].name
        return None
    
    def get_states(self, obj):
        if (States.objects.filter(id=obj.states_id).count() > 0):
            return States.objects.filter(id=obj.states_id)[0].name
        return None
    
    def get_users_tech(self, obj):
        if (Users.objects.filter(id=obj.users_tech_id).count() > 0):
            return Users.objects.filter(id=obj.users_tech_id)[0].name
        return None
    
    class Meta:
        model = Cables
        fields = ['id', 'name' , 'cabletypes', 'states', 'users_tech', 'otherserial' , 'color'
                  , 'items_endpoint_b', 'items_endpoint_a', 'sockets_endpoint_b', 'sockets_endpoint_a']

class CablestrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cablestrands
        fields = '__all__'

class CabletypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabletypes
        fields = '__all__'

class CablesSerializer(serializers.ModelSerializer):
    entities = EntitiesSerializer(required=False)
    users_tech = UsersSerializer(required=False)
    cablestrands = CablestrandsSerializer(required=False)
    cabletypes = CabletypesSerializer(required=False)
    states = StatesSerializer(required=False)

    class Meta:
        model = Cables
        fields = '__all__'




