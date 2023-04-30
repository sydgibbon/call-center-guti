
from rest_framework import serializers  # import de serializers
from assets.models import Passivedcequipmenttypes, Passivedcequipmentmodels

class GetPassivedcequipmenttypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passivedcequipmenttypes
        fields = ['id', 'name']

class GetPassivedcequipmentmodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passivedcequipmentmodels
        fields = ['id', 'name']