
from rest_framework import serializers  # import de serializers
from assets.models import Devicesimcards, Lines

class GetDevicesimcardsSelectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='designation')
    class Meta:
        model = Devicesimcards
        fields = ['id', 'name']

class GetLinesSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lines
        fields = ['id', 'name']