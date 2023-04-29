from rest_framework import serializers  # import de serializers
from assets.models import Cartridges

class GetCartridgesSelectSerializer(serializers.ModelSerializer):
    model = Cartridges
    fields = ('id', 'name')