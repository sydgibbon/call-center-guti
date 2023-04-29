from rest_framework import serializers  # import de serializers
from assets.models import Locations

class GetLocationsNameSerializer(serializers.ModelSerializer):
    model = Locations
    fields = ('id', 'name')