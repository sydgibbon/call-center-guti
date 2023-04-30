from rest_framework import serializers  # import de serializers
from assets.models import Consumableitemtypes

class GetConsumableitemtypesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumableitemtypes
        fields = ['id', 'name']