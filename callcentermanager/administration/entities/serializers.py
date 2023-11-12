from assets.models import Entities
from rest_framework import serializers

class GetEntitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entities
        fields = ['id', 'completename']