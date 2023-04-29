
from rest_framework import serializers  # import de serializers
from assets.models import States

class GetStatesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = ['id', 'name']