
from rest_framework import serializers  # import de serializers
from assets.models import Racktypes, Rackmodels, Dcrooms

class GetRacktypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Racktypes
        fields = ['id', 'name']

class GetRackmodelsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rackmodels
        fields = ['id', 'name']

class GetDcroomsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dcrooms
        fields = ['id', 'name']