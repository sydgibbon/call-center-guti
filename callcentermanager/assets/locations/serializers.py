
from rest_framework import serializers  # import de serializers
from assets.models import Locations

class GetLocationsSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ['id', 'name']

class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'