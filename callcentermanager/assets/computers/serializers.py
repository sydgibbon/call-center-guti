
from rest_framework import serializers  # import de serializers
from assets.models import Computermodels, Computertypes
from assets.groups import serializers as groupsSerializers
from assets.users import serializers as usersSerializers
from assets.states import serializers as statesSerializers
from assets.manufacturers import serializers as manufacturersSerializers
from assets.locations import serializers as locationsSerializers
from assets.networks import serializers as networksSerializers
from assets.autoupdatesystems import serializers as autoupdatesystemsSerializers

class GetComputertypesSelectSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    def get_name(self, obj):
        return obj.name
    class Meta:
        model = Computertypes
        fields = ['id', 'name']

class GetComputermodelsSelectSerializer(serializers.ModelSerializer):
    model = Computermodels
    fields = ('id', 'name')

class GetComputersDropdownSerializer(serializers.Serializer):
    computertypes = GetComputertypesSelectSerializer(many=True)
    computermodels =  GetComputermodelsSelectSerializer(many=True)
    states = statesSerializers.GetStatesNameSerializer(many=True)
    manufacturers = manufacturersSerializers.GetManufacturersNameSerializer(many=True)
    locations =  locationsSerializers.GetLocationsNameSerializer(many=True)
    users =  usersSerializers.GetUsersNameSerializer(many=True)
    groups =  groupsSerializers.GetGroupsNameSerializer(many=True)
    networks =  networksSerializers.GetNetworksNameSerializer(many=True)
    autoupdatesystems =  autoupdatesystemsSerializers.GetAutoupdatesystemsNameSerializer(many=True)

