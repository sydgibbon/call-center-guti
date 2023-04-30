
from rest_framework import serializers  # import de serializers
from assets.models import Pdutypes, Pdumodels

class GetPdutypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdutypes
        fields = ['id', 'name']

class GetPdumodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdumodels
        fields = ['id', 'name']