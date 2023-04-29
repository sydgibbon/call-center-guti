from rest_framework import serializers  # import de serializers
from assets.models import Networks

class GetNetworksNameSerializer(serializers.ModelSerializer):
    model = Networks
    fields = ('id', 'name')