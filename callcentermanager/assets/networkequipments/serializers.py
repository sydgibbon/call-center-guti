
from rest_framework import serializers  # import de serializers
from assets.models import Networkequipmenttypes, Networkequipmentmodels

class GetNetworkequipmenttypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networkequipmenttypes
        fields = ['id', 'name']

class GetNetworkequipmentmodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networkequipmentmodels
        fields = ['id', 'name']