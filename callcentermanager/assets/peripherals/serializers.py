from rest_framework import serializers  # import de serializers
from assets.models import Peripheraltypes, Peripheralmodels

class GetPeripheraltypesSerializer(serializers.ModelSerializer):
    model = Peripheraltypes
    fields = ('id', 'name')

class GetPeripheralmodelsSerializer(serializers.ModelSerializer):
    model = Peripheralmodels
    fields = ('id', 'name')