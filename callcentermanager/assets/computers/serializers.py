
from rest_framework import serializers  # import de serializers
from assets.models import Computermodels, Computertypes
class GetComputertypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computertypes
        fields = ['id', 'name']

class GetComputermodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computermodels
        fields = ['id', 'name']