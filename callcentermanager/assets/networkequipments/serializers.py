
from rest_framework import serializers  # import de serializers
from assets.models import Networkequipments, Networkequipmenttypes, Networkequipmentmodels

class GetNetworkequipmentsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networkequipments
        fields = ['id', 'name']

class GetNetworkequipmenttypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networkequipmenttypes
        fields = ['id', 'name']

class GetNetworkequipmentmodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networkequipmentmodels
        fields = ['id', 'name']