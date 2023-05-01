from rest_framework import serializers  # import de serializers
from assets.models import Cartridgeitemtypes

class GetCartridgeitemtypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartridgeitemtypes
        fields = ['id', 'name']