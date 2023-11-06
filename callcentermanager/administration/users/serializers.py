from assets.models import Locations, Users
from rest_framework import serializers


class GetUsersSerializer(serializers.ModelSerializer):
    locations = serializers.SerializerMethodField()
    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'phone', 'locations', 'is_active']

    def get_locations(self, obj):
        locations = Locations.objects.filter(id=obj.locations_id)
        if (locations.count() > 0):
            return Locations.objects.filter(id=obj.locations_id)[0].name
        return None