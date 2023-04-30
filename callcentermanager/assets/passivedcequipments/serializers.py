
from rest_framework import serializers  # import de serializers
from assets.models import Passivedcequipments, Passivedcequipmenttypes, Passivedcequipmentmodels

class GetPassivedcequipmentsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passivedcequipments
        fields = ['id', 'name']

class GetPassivedcequipmenttypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passivedcequipmenttypes
        fields = ['id', 'name']

class GetPassivedcequipmentmodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passivedcequipmentmodels
        fields = ['id', 'name']