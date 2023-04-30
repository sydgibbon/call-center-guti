
from rest_framework import serializers  # import de serializers
from assets.models import Networks

class GetNetworksSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networks
        fields = ['id', 'name']