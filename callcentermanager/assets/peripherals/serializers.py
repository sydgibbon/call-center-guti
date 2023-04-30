from rest_framework import serializers  # import de serializers
from assets.models import Peripheraltypes, Peripheralmodels

class GetPeripheraltypesSelectSerializer(serializers.ModelSerializer):
    model = Peripheraltypes
    fields = ('id', 'name')

class GetPeripheralmodelsSelectSerializer(serializers.ModelSerializer):
    model = Peripheralmodels
    fields = ('id', 'name')