from rest_framework import serializers  # import de serializers
from assets.models import Peripheraltypes, Peripheralmodels

class GetPeripheraltypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peripheraltypes
        fields = ['id', 'name']
class GetPeripheralmodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peripheralmodels
        fields = ['id', 'name']